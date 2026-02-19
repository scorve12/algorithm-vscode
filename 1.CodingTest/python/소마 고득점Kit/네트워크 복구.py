"""
[네트워크 복구] - 그래프 + 위상정렬 + BFS

문제 설명:
n개의 서버와 서버 간 의존 관계가 주어집니다.
서버 A가 서버 B에 의존하면, B가 복구된 후에야 A를 복구할 수 있습니다.
각 서버의 자체 복구 시간이 주어질 때, 모든 서버를 복구하는 최소 시간을 구하세요.
(의존하지 않는 서버들은 동시에 복구 가능)

제한사항:
- 서버 수 n은 1 이상 10,000 이하
- 의존 관계에 사이클 없음
- times[i]는 i번 서버의 자체 복구 시간
- deps는 [A, B] 형태 (A가 B에 의존)

입출력 예:
n=5, times=[1,2,3,2,1], deps=[[1,0],[2,0],[3,1],[3,2],[4,3]]
→ 8  (0→2→3→4 경로: 1+3+2+1=7 또는 0→1→3→4: 1+2+2+1=6, 최대=7... 아래 참고)
"""

from collections import deque, defaultdict


def solution(n, times, deps):
    graph = defaultdict(list)  # 선행 → 후행
    in_degree = [0] * n
    earliest = [0] * n  # 각 서버가 복구 완료되는 가장 빠른 시간

    for a, b in deps:
        graph[b].append(a)  # b 완료 후 a 복구 가능
        in_degree[a] += 1

    # 위상 정렬 + 최장 경로 (Critical Path)
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            earliest[i] = times[i]
            queue.append(i)

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            # nxt의 시작 시간은 모든 선행 노드 중 가장 늦게 끝나는 시간
            earliest[nxt] = max(earliest[nxt], earliest[node] + times[nxt])
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return max(earliest)


# 테스트
assert solution(5, [1, 2, 3, 2, 1], [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) == 7
assert solution(3, [3, 2, 1], []) == 3  # 모두 독립 → 동시 복구
assert solution(3, [1, 1, 1], [[1, 0], [2, 1]]) == 3  # 직렬
print("네트워크 복구: 모든 테스트 통과!")
