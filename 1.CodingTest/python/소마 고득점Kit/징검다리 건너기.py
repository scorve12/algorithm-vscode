"""
[징검다리 건너기] - 이분탐색 + 슬라이딩 윈도우

문제 설명:
일렬로 놓인 디딤돌이 있고, 각 디딤돌에는 숫자가 적혀 있습니다.
한 번 밟을 때마다 숫자가 1씩 줄어들고, 0이 되면 밟을 수 없습니다.
한 번에 최대 k칸까지 점프할 수 있을 때, 최대 몇 명이 건널 수 있는지 구하세요.

제한사항:
- stones의 길이는 1 이상 200,000 이하
- 각 원소는 1 이상 200,000,000 이하
- k는 1 이상 stones의 길이 이하

입출력 예:
stones=[2,4,5,3,2,1,4,2,5,1], k=3 → 3
"""


def solution(stones, k):
    def can_cross(mid):
        # mid명이 건널 수 있는지 확인
        # 연속으로 k개 이상 0 이하가 되면 건널 수 없음
        consecutive = 0
        for s in stones:
            if s - mid < 0:
                consecutive += 1
                if consecutive >= k:
                    return False
            else:
                consecutive = 0
        return True

    lo, hi = 1, max(stones)
    answer = 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if can_cross(mid):
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return answer


# 테스트
assert solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3) == 3
assert solution([1, 1, 1], 1) == 1
print("징검다리 건너기: 모든 테스트 통과!")
