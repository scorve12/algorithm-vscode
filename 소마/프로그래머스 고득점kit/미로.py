from collections import deque

def solution(maze):
    R, C = len(maze), len(maze[0])
    
    # 1. 상하좌우 이동을 위한 방향 벡터 (y축, x축)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # 2. 시작점(S) 찾기 및 초기화
    start_y, start_x = 0, 0
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start_y, start_x = r, c

    # 3. 큐와 방문 기록 준비
    queue = deque([(start_y, start_x, 1)]) # (y, x, 현재까지의 거리)
    visited = [[False] * C for _ in range(R)]
    visited[start_y][start_x] = True # 시작점 방문 처리

    # 4. 탐색 시작
    while queue:
        y, x, dist = queue.popleft() # 큐에서 현재 위치 꺼내기

        if maze[y][x] == 'E': # 도착했다면 거리 반환
            return dist

        # 5. 인접한 상하좌우 좌표 검사
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 유효성 검사: 맵 안인가? AND 벽이 아닌가? AND 방문 안 했나?
            if 0 <= ny < R and 0 <= nx < C:
                if maze[ny][nx] != '1' and not visited[ny][nx]:
                    visited[ny][nx] = True      # 방문 표시 (중요!)
                    queue.append((ny, nx, dist + 1)) # 다음 탐색지로 예약
                    
    return -1 # 끝까지 못 찾은 경우

print(solution(["S0010", "00010", "00100", "000E0"]))
