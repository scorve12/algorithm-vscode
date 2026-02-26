from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = deque.popleft()
        
        for i in range(4):
                
            next_x, next_y = x + move_x[i], y + move_y[i]
                
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y]:
                    
                if next_x == 0 and next_y == 0: continue
                    
                maps[next_x][next_y] = maps[x][y] +1
                queue.append((next_x, next_y))
                    
    answer = maps[n-1][m-1]
    return answer if answer > 1 else -1

test =[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(test))
