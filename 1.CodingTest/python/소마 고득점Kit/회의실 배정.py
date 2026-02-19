"""
[회의실 배정] - 그리디 + 힙(우선순위 큐)

문제 설명:
회의 일정이 [시작시간, 종료시간] 형태로 주어질 때,
모든 회의를 진행하기 위해 필요한 최소 회의실 수를 구하세요.

제한사항:
- 회의의 수는 1 이상 100,000 이하
- 시작시간과 종료시간은 0 이상 1,000,000 이하
- 시작시간 < 종료시간

입출력 예:
[[0,30],[5,10],[15,20]] → 2
[[7,10],[2,4]] → 1
[[0,5],[5,10],[10,15]] → 1
[[1,5],[2,6],[3,7],[4,8]] → 4
"""

import heapq


def solution(meetings):
    if not meetings:
        return 0

    meetings.sort(key=lambda x: x[0])  # 시작시간 기준 정렬
    rooms = []  # 각 회의실의 종료시간을 저장하는 최소 힙

    for start, end in meetings:
        # 가장 빨리 끝나는 회의실이 현재 회의 시작 전에 끝나면 재사용
        if rooms and rooms[0] <= start:
            heapq.heapreplace(rooms, end)
        else:
            heapq.heappush(rooms, end)

    return len(rooms)


# 테스트
assert solution([[0, 30], [5, 10], [15, 20]]) == 2
assert solution([[7, 10], [2, 4]]) == 1
assert solution([[0, 5], [5, 10], [10, 15]]) == 1
assert solution([[1, 5], [2, 6], [3, 7], [4, 8]]) == 4
print("회의실 배정: 모든 테스트 통과!")
