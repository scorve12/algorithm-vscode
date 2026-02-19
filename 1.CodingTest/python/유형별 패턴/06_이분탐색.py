"""
이분 탐색 (Binary Search) 패턴 정리
- 정렬된 데이터에서 O(log n) 탐색
- 매개변수 탐색: 최적값을 이분 탐색으로 찾기
- 활용: 값 찾기, 범위 찾기, 최적화 문제
"""
import bisect


# ============================================================
# 1. 기본 이분 탐색
# ============================================================
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 못 찾음


# ============================================================
# 2. Lower Bound / Upper Bound
# ============================================================
# Lower Bound: target 이상인 첫 번째 위치
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Upper Bound: target 초과인 첫 번째 위치
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

# bisect 모듈 활용 (동일 기능)
arr = [1, 2, 2, 2, 3, 4, 5]
bisect.bisect_left(arr, 2)   # 1 (lower bound)
bisect.bisect_right(arr, 2)  # 4 (upper bound)

# target의 개수 세기
def count_target(arr, target):
    return bisect.bisect_right(arr, target) - bisect.bisect_left(arr, target)


# ============================================================
# 3. 매개변수 탐색 (Parametric Search)
# ============================================================
# "조건을 만족하는 최솟값/최댓값을 찾아라"
# → 특정 값이 가능한지 판별하는 함수 + 이분 탐색

# 예: 나무 자르기 - 높이 H로 잘라서 M 이상 나무를 얻는 최대 H
def cut_trees(trees, M):
    left, right = 0, max(trees)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        total = sum(max(0, t - mid) for t in trees)
        if total >= M:
            result = mid       # 가능하니 더 높이 시도
            left = mid + 1
        else:
            right = mid - 1    # 불가능하니 낮추기
    return result


# ============================================================
# 4. 회전 정렬 배열에서 탐색
# ============================================================
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # 왼쪽 절반이 정렬된 경우
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 오른쪽 절반이 정렬된 경우
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# ============================================================
# 5. 실수 범위 이분 탐색
# ============================================================
def sqrt_binary(n, eps=1e-9):
    left, right = 0, n
    while right - left > eps:
        mid = (left + right) / 2
        if mid * mid < n:
            left = mid
        else:
            right = mid
    return (left + right) / 2


# ============================================================
# 6. 2D 행렬 이분 탐색
# ============================================================
def search_matrix(matrix, target):
    """행렬이 좌→우, 위→아래 정렬된 경우"""
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# ============================================================
# 7. bisect 활용 - LIS (최장 증가 부분 수열) O(n log n)
# ============================================================
def lis_length(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


# ============================================================
# 핵심 정리
# ============================================================
# - left <= right: 값 찾기 (정확한 값)
# - left < right: 범위 찾기 (lower/upper bound)
# - 매개변수 탐색: is_possible(mid) 함수 만들기 → 이분 탐색
# - bisect_left/bisect_right: 정렬된 리스트에서 삽입 위치
# - 실수 이분 탐색: eps(오차 범위)로 종료 조건 설정
# - 시간복잡도: O(log n)
