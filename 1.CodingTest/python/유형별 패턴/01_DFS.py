"""
DFS (깊이 우선 탐색) 패턴 정리
- 그래프/트리를 깊이 방향으로 탐색
- 스택 또는 재귀로 구현
- 활용: 경로 탐색, 연결 요소, 백트래킹, 순열/조합
"""

# ============================================================
# 1. 기본 DFS - 재귀 (인접 리스트)
# ============================================================
def dfs_recursive(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# 사용 예시
graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
visited = set()
dfs_recursive(graph, 1, visited)


# ============================================================
# 2. 기본 DFS - 스택 (반복)
# ============================================================
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited


# ============================================================
# 3. 2D 격자 DFS (상하좌우 탐색)
# ============================================================
def dfs_grid(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if (r, c) in visited or grid[r][c] == 0:
        return

    visited.add((r, c))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        dfs_grid(grid, r + dr[i], c + dc[i], visited)

# 섬의 개수 세기 예시
def count_islands(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1 and (r, c) not in visited:
                dfs_grid(grid, r, c, visited)
                count += 1
    return count


# ============================================================
# 4. 백트래킹 DFS (순열/조합)
# ============================================================

# 순열 (Permutation)
def permutations(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], nums)
    return result

# 조합 (Combination)
def combinations(nums, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


# ============================================================
# 5. 경로 존재 여부 확인
# ============================================================
def has_path(graph, start, end):
    visited = set()
    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False
    return dfs(start)


# ============================================================
# 6. 모든 경로 찾기
# ============================================================
def find_all_paths(graph, start, end):
    result = []
    def dfs(node, path):
        if node == end:
            result.append(path[:])
            return
        for neighbor in graph[node]:
            if neighbor not in path:  # 방문 체크를 path로
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
    dfs(start, [start])
    return result


# ============================================================
# 7. 사이클 탐지 (방향 그래프)
# ============================================================
def has_cycle(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:  # 순환 발견
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    return False


# ============================================================
# 핵심 정리
# ============================================================
# - 재귀 DFS: 코드가 간결, 파이썬 재귀 제한(sys.setrecursionlimit) 주의
# - 스택 DFS: 재귀 깊이 제한 없음, 명시적 스택 사용
# - 격자 DFS: dr, dc 배열로 4방향/8방향 이동
# - 백트래킹: path에 추가 → 재귀 → path에서 제거
# - 시간복잡도: O(V + E) (정점 + 간선)
