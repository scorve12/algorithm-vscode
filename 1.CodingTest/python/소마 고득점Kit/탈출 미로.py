"""
[탈출 미로] - BFS + 비트마스킹 (상태 관리)

문제 설명:
N×M 미로에서 시작점 'S'에서 출구 'E'까지 이동합니다.
미로에는 열쇠('a'~'d')와 문('A'~'D')이 있습니다.
- 대응하는 열쇠를 가져야 문을 통과할 수 있습니다.
- '#'은 벽, '.'은 빈 칸입니다.
최소 이동 횟수를 구하세요. 탈출 불가능하면 -1을 반환합니다.

제한사항:
- 1 ≤ N, M ≤ 50
- 열쇠와 문은 각각 최대 4종류 (a~d, A~D)

입출력 예:
maze = ["SaA.E"] → 4
"""

from collections import deque


def solution(maze):
    n = len(maze)
    m = len(maze[0])

    # 시작점 찾기
    sr = sc = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                sr, sc = i, j

    # BFS: (row, col, 열쇠 비트마스크)
    # 열쇠 a~d → 비트 0~3
    visited = set()
    visited.add((sr, sc, 0))
    queue = deque([(sr, sc, 0, 0)])  # r, c, keys, moves

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, keys, moves = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            cell = maze[nr][nc]
            if cell == '#':
                continue

            new_keys = keys

            # 문인 경우: 해당 열쇠가 있어야 통과
            if 'A' <= cell <= 'D':
                if not (keys & (1 << (ord(cell) - ord('A')))):
                    continue

            # 열쇠인 경우: 비트마스크에 추가
            if 'a' <= cell <= 'd':
                new_keys = keys | (1 << (ord(cell) - ord('a')))

            # 출구 도달
            if cell == 'E':
                return moves + 1

            state = (nr, nc, new_keys)
            if state not in visited:
                visited.add(state)
                queue.append((nr, nc, new_keys, moves + 1))

    return -1


# 테스트 1: 1차원 미로 - 열쇠 a로 문 A를 열어야 함
assert solution(["SaA.E"]) == 4

# 테스트 2: 열쇠 없이 갈 수 있는 경우
assert solution([
    "S...",
    "...E",
]) == 4

# 테스트 3: 벽으로 막혀 열쇠+문 경로만 가능
assert solution([
    "S.a",
    "##.",
    "...",
    ".#A",
    "..E",
]) == 6

# 테스트 4: 탈출 불가능
assert solution([
    "S#E",
    ".#.",
    ".#.",
]) == -1

# 테스트 5: 여러 열쇠가 필요한 경우
assert solution(["SaAbBE"]) == 5

print("탈출 미로: 모든 테스트 통과!")
