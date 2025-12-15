#배열조작
arr = [1, 2, 3, 4, 5]

double_arr = [[1,2],[2,3],[3,4],[4,5]]
filetered = [ x for x in arr if x > 2]

#정렬 (커스텀)
double_arr.sort(key=lambda x: (x[0], -x[1]))

print(arr)
print(double_arr)
print(filetered)

#딕셔너리 기본값
from collections import defaultdict
graph = defaultdict(list)

#라이브러리
from collections import deque, Counter
from itertools import combinations, permutations
from heapq import heappush, heappop
import bisect


import sys
input = sys.stdin.readline
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import combinations, permutations
import bisect

# 입력 패턴
n = int(input())
arr = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]

# DFS 템플릿
def dfs(node, visited):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, visited)

# BFS 템플릿
def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

# DP 템플릿
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

# 1. PyPy3로 제출
some_list = []

# 2. 입출력 최적화
import sys
input = sys.stdin.readline
print = sys.stdout.write  # 대량 출력 시

