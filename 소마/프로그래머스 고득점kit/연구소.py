#백준 14502 연구소
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# --- 1. 입력 받기 ---
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 빈칸(0)과 바이러스(2) 위치 미리 저장하기
empty = []
virus = []
for r in range(n):
    for c in range(m):
        if graph[r][c] == 0:
            empty.append((r, c))
        elif graph[r][c] == 2:
            virus.append((r, c))

# --- 2. BFS 함수 정의 ---
def get_safe_area(temp_graph):
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: # 상하좌우
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and temp_graph[nr][nc] == 0:
                temp_graph[nr][nc] = 2 # 바이러스 전파
                q.append((nr, nc))
    
    # 안전 영역(0) 개수 세기
    return sum(row.count(0) for row in temp_graph)

# --- 3. 조합으로 벽 세우기 및 시뮬레이션 ---
result = 0
for walls in combinations(empty, 3):
    # 맵 복사 (매번 초기 상태에서 시작해야 함)
    # 2차원 리스트 복사는 리스트 컴프리헨션이 deepcopy보다 빠릅니다!
    test_graph = [row[:] for row in graph]
    
    # 벽 3개 설치
    for wr, wc in walls:
        test_graph[wr][wc] = 1
    
    # BFS 결과 중 최댓값 갱신
    result = max(result, get_safe_area(test_graph))

print(result)