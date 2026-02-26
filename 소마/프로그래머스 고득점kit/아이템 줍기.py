from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    queue = deque([(characterX, characterY)])
    end_node = [(itemX, itemY)]
    
    move_x = [1, -1, 0, 0]
    move_y = [0, 0, -1, 1]
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            next_x, next_y = x + move_x[i], y + move_y[i]

            #사각형 사이에 있는가? [왼쪽아래x, 왼쪽아래y, 오른쪽위x, 오른쪽위y]
            for left_down_x, left_down_y, right_up_x, right_up_y in zip(rectangle):
                if left_down_x < next_x < right_up_y and left_down_y < next_y < right_up_x:
                    queue.append(next_x, next_y)
        
        
        
    
    
    return answer