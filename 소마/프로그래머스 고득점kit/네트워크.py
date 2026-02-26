# 네트워크 43162번 문제

def solution(n, computers):
    answer = 0
    visited = set()

    def dfs(i):
        visited.add(i)
        for next_com, connected in enumerate(computers[i]):
            if connected and next_com not in visited:
                dfs(next_com)

    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1  # DFS가 한 번 끝날 때마다 네트워크 1개 추가
    return answer