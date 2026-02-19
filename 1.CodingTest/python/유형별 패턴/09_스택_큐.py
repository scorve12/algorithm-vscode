"""
스택 & 큐 패턴 정리
- 스택: LIFO (후입선출), 리스트로 구현
- 큐: FIFO (선입선출), deque로 구현
- 활용: 괄호 검증, 모노톤 스택, 슬라이딩 윈도우 최대
"""
from collections import deque


# ============================================================
# 1. 스택 기본 연산
# ============================================================
stack = []
stack.append(1)      # push
stack.append(2)
top = stack[-1]      # peek (2)
val = stack.pop()    # pop (2)
is_empty = len(stack) == 0


# ============================================================
# 2. 괄호 유효성 검사
# ============================================================
def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0


# ============================================================
# 3. 모노톤 스택 (Monotone Stack)
# ============================================================
# 다음 큰 수 (Next Greater Element)
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # 인덱스를 저장
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result

# 이전 작은 수 (Previous Smaller Element)
def prev_smaller(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)
    return result


# ============================================================
# 4. 히스토그램 최대 넓이 (모노톤 스택 응용)
# ============================================================
def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights.append(0)  # 센티넬
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()  # 센티넬 제거
    return max_area


# ============================================================
# 5. 큐 기본 연산
# ============================================================
queue = deque()
queue.append(1)       # enqueue (오른쪽)
queue.append(2)
val = queue.popleft()  # dequeue (왼쪽, 1)
front = queue[0]       # peek


# ============================================================
# 6. 슬라이딩 윈도우 최댓값 (모노톤 데크)
# ============================================================
def max_sliding_window(nums, k):
    dq = deque()  # 인덱스 저장, 값은 내림차순 유지
    result = []
    for i in range(len(nums)):
        # 윈도우 밖의 인덱스 제거
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # 현재 값보다 작은 값 제거
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


# ============================================================
# 7. 스택으로 큐 구현 / 큐로 스택 구현
# ============================================================
class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]


# ============================================================
# 8. 문자열 디코딩 (스택 응용)
# ============================================================
def decode_string(s):
    """예: "3[a2[c]]" → "accaccacc" """
    stack = []
    curr_str = ""
    curr_num = 0
    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif char == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += char
    return curr_str


# ============================================================
# 핵심 정리
# ============================================================
# 스택:
# - list.append() / list.pop() → O(1)
# - 괄호 문제, 후위 표기법, 재귀 시뮬레이션
# - 모노톤 스택: 다음/이전 큰/작은 수 → O(n)
#
# 큐:
# - deque.append() / deque.popleft() → O(1)
# - BFS 탐색의 기본 자료구조
# - 모노톤 데크: 슬라이딩 윈도우 최대/최소 → O(n)
