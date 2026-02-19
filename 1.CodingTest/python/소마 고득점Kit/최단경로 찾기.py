"""
[최단경로 찾기] - 다익스트라 알고리즘

문제 설명:
방향 가중치 그래프에서 시작 노드로부터 모든 노드까지의 최단 거리를 구하세요.
도달할 수 없는 노드는 -1로 표시합니다.

제한사항:
- 노드의 수 n은 1 이상 20,000 이하
- 간선의 수는 1 이상 300,000 이하
- 간선 가중치는 1 이상 10 이하
- edges는 [출발, 도착, 가중치] 형태

입출력 예:
n=6, start=1
edges=[[1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
→ [0, 2, 3, 1, 2, 4]  (1번 노드 기준)
"""

import heapq
from collections import defaultdict

INF = float('inf')


def solution(n, start, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (거리, 노드)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    result = []
    for i in range(1, n + 1):
        result.append(dist[i] if dist[i] != INF else -1)

    return result


# 테스트
edges = [
    [1, 2, 2], [1, 3, 5], [1, 4, 1],
    [2, 3, 3], [2, 4, 2],
    [3, 2, 3], [3, 6, 5],
    [4, 3, 3], [4, 5, 1],
    [5, 3, 1], [5, 6, 2],
]
assert solution(6, 1, edges) == [0, 2, 3, 1, 2, 4]
assert solution(3, 1, [[1, 2, 1]]) == [0, 1, -1]
print("최단경로 찾기: 모든 테스트 통과!")
