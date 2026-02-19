"""
BFS (너비 우선 탐색) 패턴 정리
- 그래프/트리를 너비 방향으로 탐색
- 큐(deque)로 구현
- 활용: 최단 거리, 레벨별 탐색, 최소 횟수
"""
from collections import deque


# ============================================================
# 1. 기본 BFS (인접 리스트)
# ============================================================
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


# ============================================================
# 2. 최단 거리 BFS (가중치 없는 그래프)
# ============================================================
def shortest_path(graph, start, end):
    visited = set([start])
    queue = deque([(start, 0)])  # (노드, 거리)
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1  # 도달 불가


# ============================================================
# 3. 2D 격자 BFS (최단 거리)
# ============================================================
def bfs_grid(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    er, ec = end
    visited = set()
    visited.add((sr, sc))
    queue = deque([(sr, sc, 0)])  # (행, 열, 거리)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, dist = queue.popleft()
        if r == er and c == ec:
            return dist
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] != 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    return -1


# ============================================================
# 4. 레벨별 BFS (트리 레벨 순회)
# ============================================================
def level_order(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        level_size = len(queue)  # 현재 레벨의 노드 수
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        result.append(current_level)
    return result


# ============================================================
# 5. 다차원 BFS (상태 공간 탐색)
# ============================================================
# 예: 자물쇠 문제 - "0000"에서 target까지 최소 회전 수
def open_lock(deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1

    visited = set(["0000"])
    queue = deque([("0000", 0)])

    while queue:
        state, turns = queue.popleft()
        if state == target:
            return turns
        for i in range(4):
            for d in [-1, 1]:
                digit = (int(state[i]) + d) % 10
                new_state = state[:i] + str(digit) + state[i+1:]
                if new_state not in visited and new_state not in dead:
                    visited.add(new_state)
                    queue.append((new_state, turns + 1))
    return -1


# ============================================================
# 6. 양방향 BFS (시작/끝 동시 탐색)
# ============================================================
def bidirectional_bfs(graph, start, end):
    if start == end:
        return 0

    front = {start}
    back = {end}
    visited = {start, end}
    dist = 0

    while front and back:
        dist += 1
        # 항상 작은 쪽을 확장
        if len(front) > len(back):
            front, back = back, front

        next_front = set()
        for node in front:
            for neighbor in graph[node]:
                if neighbor in back:
                    return dist
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_front.add(neighbor)
        front = next_front
    return -1


# ============================================================
# 7. 0-1 BFS (가중치 0 또는 1인 그래프)
# ============================================================
def bfs_01(graph, start, n):
    """graph[node] = [(neighbor, weight)] where weight is 0 or 1"""
    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque([start])

    while dq:
        node = dq.popleft()
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                if weight == 0:
                    dq.appendleft(neighbor)  # 가중치 0은 앞에
                else:
                    dq.append(neighbor)       # 가중치 1은 뒤에
    return dist


# ============================================================
# 핵심 정리
# ============================================================
# - BFS는 가중치 없는 그래프에서 최단 거리 보장
# - deque 사용 필수 (list.pop(0)은 O(n), deque.popleft()는 O(1))
# - visited는 큐에 넣을 때 체크 (꺼낼 때 X) → 중복 방문 방지
# - 레벨별 처리: len(queue)로 현재 레벨 크기 저장 후 반복
# - 시간복잡도: O(V + E)
