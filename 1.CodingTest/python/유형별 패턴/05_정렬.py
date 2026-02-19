"""
정렬 (Sorting) 패턴 정리
- 파이썬 내장 정렬: Timsort O(n log n)
- 활용: 커스텀 정렬, 비교 기반 문제, 그리디 전처리
"""
from functools import cmp_to_key


# ============================================================
# 1. 기본 정렬
# ============================================================
arr = [3, 1, 4, 1, 5, 9]

arr.sort()                    # 제자리 정렬 (원본 변경)
sorted_arr = sorted(arr)      # 새 리스트 반환 (원본 유지)
arr.sort(reverse=True)        # 내림차순


# ============================================================
# 2. key 함수 활용
# ============================================================
# 절댓값 기준 정렬
nums = [-3, 1, -2, 4]
nums.sort(key=abs)  # [1, -2, -3, 4]

# 문자열 길이 기준
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)

# 튜플의 특정 원소 기준
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
pairs.sort(key=lambda x: x[1])  # 두 번째 원소 기준

# 다중 조건 정렬
students = [("Kim", 90), ("Lee", 85), ("Park", 90)]
students.sort(key=lambda x: (-x[1], x[0]))  # 점수 내림차순, 같으면 이름 오름차순


# ============================================================
# 3. 커스텀 비교 함수 (cmp_to_key)
# ============================================================
# 가장 큰 수 만들기
def largest_number(nums):
    str_nums = list(map(str, nums))
    str_nums.sort(key=cmp_to_key(lambda a, b: -1 if a+b > b+a else 1))
    return ''.join(str_nums).lstrip('0') or '0'

# 예: [3, 30, 34, 5, 9] → "9534330"


# ============================================================
# 4. 카운팅 정렬 (범위가 작을 때 O(n))
# ============================================================
def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i in range(max_val + 1):
        result.extend([i] * count[i])
    return result

# Counter 활용
from collections import Counter
def frequency_sort(s):
    """빈도 기준 내림차순 정렬"""
    counter = Counter(s)
    return ''.join(sorted(s, key=lambda c: -counter[c]))


# ============================================================
# 5. 정렬 활용 패턴
# ============================================================

# 5-1. 두 배열 비교 (아나그램 확인)
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# 5-2. 겹치는 구간 병합
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

# 5-3. 회의실 문제 (그리디 + 정렬)
def min_meeting_rooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = 0
    end_ptr = 0
    for start in starts:
        if start < ends[end_ptr]:
            rooms += 1
        else:
            end_ptr += 1
    return rooms


# ============================================================
# 6. 안정 정렬 활용
# ============================================================
# 파이썬 sort()는 안정 정렬 → 같은 키의 원래 순서 유지
# 여러 번 정렬하여 다중 기준 구현 가능
data = [(1, 'c'), (2, 'a'), (1, 'b'), (2, 'b')]
data.sort(key=lambda x: x[1])  # 먼저 부 기준으로 정렬
data.sort(key=lambda x: x[0])  # 다음 주 기준으로 정렬
# 결과: [(1, 'b'), (1, 'c'), (2, 'a'), (2, 'b')]


# ============================================================
# 핵심 정리
# ============================================================
# - sort(): 제자리, sorted(): 새 리스트
# - key=lambda로 정렬 기준 지정, 내림차순은 -부호 또는 reverse=True
# - cmp_to_key: 두 원소 간 비교 로직이 복잡할 때
# - 안정 정렬: 같은 키의 상대 순서 유지 (다중 기준에 유리)
# - 정렬 전처리 후 그리디/투포인터 조합이 빈출
# - 시간복잡도: O(n log n), 카운팅 정렬은 O(n + k)
