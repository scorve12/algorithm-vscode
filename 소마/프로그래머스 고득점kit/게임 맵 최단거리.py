from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])# 시작점 (0, 0)을 큐에 추가
    #시작은 0,0 도착은 n-1, m-1으로 고정되어 있다.

    while queue:
        # 0,0에서 시작해서 상하좌우로 이동할 수 있는 좌표를 큐에 추가하면서 탐색
        # 처음 들어간 0,0부터 시작 
        x, y = queue.popleft()# 현재 위치에서 상하좌우로 이동할 수 있는 좌표를 계산하기 위해 반복
        
        for i in range(4):# 상하좌우로 이동할 때의 이동 가능 하면 큐에 추가
            # nx = 다음 x좌표, ny = 다음 y좌표
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if nx == 0 and ny == 0: continue

                maps[nx][ny] = maps[x][y] + 1# 방문한 곳의 값이 1이므로, 이전 위치의 값에 1을 더해서 거리 계산

                queue.append((nx, ny))# 다음 탐색할 좌표를 큐에 추가
                
    answer = maps[n-1][m-1]# 도착점의 값이 최단 거리이므로, 이를 반환
    return answer if answer > 1 else -1


