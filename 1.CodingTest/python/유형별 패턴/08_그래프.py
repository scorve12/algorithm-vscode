"""
그래프 (Graph) 패턴 정리
- 노드와 간선으로 구성된 자료구조
- 활용: 최단 경로, 위상 정렬, 유니온 파인드, MST
"""
from collections import defaultdict, deque
import heapq


# ============================================================
# 1. 그래프 표현
# ============================================================
# 인접 리스트 (가장 많이 사용)
graph_list = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
for u, v in edges:
    graph_list[u].append(v)
    graph_list[v].append(u)  # 무방향이면 양쪽

# 인접 행렬
n = 5
graph_matrix = [[0] * n for _ in range(n)]
for u, v in edges:
    graph_matrix[u][v] = 1
    graph_matrix[v][u] = 1


# ============================================================
# 2. 위상 정렬 (Topological Sort) - BFS (Kahn)
# ============================================================
def topological_sort(n, edges):
    """n: 노드 수, edges: [(from, to), ...]"""
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != n:
        return []  # 사이클 존재
    return result


# ============================================================
# 3. 유니온 파인드 (Union-Find / Disjoint Set)
# ============================================================
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # 이미 같은 집합
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px  # 랭크 기반 합치기
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# 활용: 연결 요소 수 세기
def count_components(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return len(set(uf.find(i) for i in range(n)))


# ============================================================
# 4. 크루스칼 알고리즘 (MST - 최소 신장 트리)
# ============================================================
def kruskal(n, edges):
    """edges: [(weight, u, v), ...]"""
    edges.sort()  # 가중치 기준 정렬
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_cost += weight
            mst_edges.append((u, v, weight))
    return mst_cost, mst_edges


# ============================================================
# 5. 벨만-포드 (음수 가중치 최단 경로)
# ============================================================
def bellman_ford(n, edges, start):
    """edges: [(u, v, weight), ...]"""
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 음수 사이클 검출
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # 음수 사이클 존재
    return dist


# ============================================================
# 6. 플로이드-워셜 (모든 쌍 최단 경로)
# ============================================================
def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# ============================================================
# 7. 이분 그래프 판별
# ============================================================
def is_bipartite(graph, n):
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True


# ============================================================
# 핵심 정리
# ============================================================
# - 인접 리스트: defaultdict(list), 메모리 효율적
# - 위상 정렬: 진입차수(indegree) + BFS, 사이클 감지 가능
# - 유니온 파인드: 경로 압축 + 랭크 → 거의 O(1)
# - 최단 경로:
#   다익스트라: 양수 가중치, O((V+E)log V)
#   벨만-포드: 음수 가중치, O(VE)
#   플로이드: 모든 쌍, O(V³)
# - MST: 크루스칼(간선 정렬 + 유니온 파인드)
