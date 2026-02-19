"""
투 포인터 & 슬라이딩 윈도우 패턴 정리
- 투 포인터: 두 개의 포인터로 범위를 좁혀가며 탐색
- 슬라이딩 윈도우: 고정/가변 크기 윈도우를 이동하며 계산
- 활용: 부분 배열, 문자열, 두 수의 합, 중복 제거
"""
from collections import defaultdict


# ============================================================
# 1. 양끝 투 포인터 (Opposite Direction)
# ============================================================
# 정렬된 배열에서 두 수의 합
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

# 물 담기 (Container With Most Water)
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0
    while left < right:
        h = min(heights[left], heights[right])
        max_water = max(max_water, h * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water


# ============================================================
# 2. 같은 방향 투 포인터 (Same Direction)
# ============================================================
# 중복 제거 (정렬된 배열)
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

# 0을 뒤로 이동
def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# ============================================================
# 3. 세 수의 합 (3Sum)
# ============================================================
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:  # 중복 건너뛰기
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result


# ============================================================
# 4. 고정 크기 슬라이딩 윈도우
# ============================================================
# 크기 k인 부분 배열의 최대 합
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # 들어오는 값 + 나가는 값
        max_sum = max(max_sum, window_sum)
    return max_sum

# 크기 k인 윈도우 내 고유 문자 수
def distinct_in_window(s, k):
    result = []
    window = defaultdict(int)
    for i in range(len(s)):
        window[s[i]] += 1
        if i >= k:
            window[s[i - k]] -= 1
            if window[s[i - k]] == 0:
                del window[s[i - k]]
        if i >= k - 1:
            result.append(len(window))
    return result


# ============================================================
# 5. 가변 크기 슬라이딩 윈도우
# ============================================================
# 합이 target 이상인 최소 길이 부분 배열
def min_subarray_len(target, nums):
    left = 0
    curr_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0

# 최대 k개의 고유 문자를 포함하는 최장 부분 문자열
def longest_k_distinct(s, k):
    window = defaultdict(int)
    left = 0
    max_len = 0
    for right in range(len(s)):
        window[s[right]] += 1
        while len(window) > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# ============================================================
# 6. 문자열 아나그램 찾기
# ============================================================
def find_anagrams(s, p):
    from collections import Counter
    result = []
    p_count = Counter(p)
    s_count = Counter()
    k = len(p)

    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= k:
            s_count[s[i - k]] -= 1
            if s_count[s[i - k]] == 0:
                del s_count[s[i - k]]
        if s_count == p_count:
            result.append(i - k + 1)
    return result


# ============================================================
# 7. 투 포인터 - 연결 리스트
# ============================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 중간 노드 찾기 (fast & slow)
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 사이클 감지 (Floyd's Algorithm)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# ============================================================
# 핵심 정리
# ============================================================
# 투 포인터:
# - 양끝: 정렬된 배열에서 합/차 문제
# - 같은 방향: 중복 제거, 파티션
# - fast & slow: 연결 리스트 중간, 사이클
#
# 슬라이딩 윈도우:
# - 고정 크기: sum += new - old
# - 가변 크기: while 조건으로 left 이동
# - 문자 빈도: Counter/defaultdict(int)
#
# - 정렬 + 투 포인터 조합이 빈출
# - 시간복잡도: O(n) (각 원소 최대 2번 처리)
