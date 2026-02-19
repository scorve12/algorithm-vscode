"""
재귀 (Recursion) 패턴 정리
- 함수가 자기 자신을 호출
- 반드시 종료 조건(base case) 필요
- 활용: 분할 정복, 트리 순회, 수학 문제, 백트래킹
"""
import sys
sys.setrecursionlimit(10**6)  # 파이썬 기본 재귀 제한: 1000


# ============================================================
# 1. 기본 재귀 패턴
# ============================================================
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ============================================================
# 2. 메모이제이션 (Top-Down DP)
# ============================================================
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# 딕셔너리 방식
def fib_dict(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_dict(n - 1, memo) + fib_dict(n - 2, memo)
    return memo[n]


# ============================================================
# 3. 분할 정복 (Divide & Conquer)
# ============================================================
# 병합 정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 거듭제곱 (분할 정복) O(log n)
def power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)


# ============================================================
# 4. 트리 재귀
# ============================================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 트리 높이
def tree_height(root):
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

# 트리 순회
def inorder(root):     # 중위: 왼 → 루트 → 오
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):    # 전위: 루트 → 왼 → 오
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):   # 후위: 왼 → 오 → 루트
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# ============================================================
# 5. 부분집합 생성 (재귀)
# ============================================================
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


# ============================================================
# 6. 문자열 재귀
# ============================================================
# 문자열 뒤집기
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# 팰린드롬 확인
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# ============================================================
# 7. 꼬리 재귀 최적화 (파이썬은 미지원이지만 패턴 참고)
# ============================================================
# 일반 재귀 → 반복으로 변환
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 재귀를 스택으로 변환하는 일반 패턴
def recursive_to_iterative_pattern():
    """
    재귀 함수:
        def f(args):
            if base_case: return result
            ... f(new_args) ...

    반복 변환:
        stack = [initial_args]
        while stack:
            args = stack.pop()
            if base_case: continue
            stack.append(new_args)
    """
    pass


# ============================================================
# 핵심 정리
# ============================================================
# - 반드시 base case를 먼저 정의
# - 파이썬 재귀 제한: sys.setrecursionlimit() 으로 조절
# - 중복 계산 → @lru_cache 또는 딕셔너리 메모이제이션
# - 재귀가 깊으면 스택 오버플로우 → 반복으로 변환 고려
# - 분할 정복: 문제를 반으로 나누어 각각 해결 후 합치기
# - 트리 문제의 대부분은 재귀로 자연스럽게 풀림
