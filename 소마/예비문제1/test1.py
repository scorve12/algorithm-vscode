# [문제 1] 지연 전파 최소화
#
# N개의 서버(1 ~ N)와 M개의 단방향 통신 링크가 있다.
# 각 링크는 (u, v, w) 형태이며, 서버 u에서 v로 신호를 보내는 데 w초가 걸린다.
#
# 당신은 정확히 K개의 서버를 "중계 서버"로 지정할 수 있다.
# 중계 서버는 신호를 받을 때마다 즉시(0초) 모든 outgoing 링크로 재전송할 수 있고,
# 일반 서버는 신호를 받을 때마다 추가로 1초의 처리 지연 후 outgoing 링크로 재전송한다.
#
# 1번 서버에서 시각 0에 신호를 시작했을 때,
# 모든 서버가 신호를 처음 받는 시간의 최댓값(=전체 전파 완료 시간)을 최소화하라.
#
# 입력 형식
# - 첫 줄: N M K
# - 다음 M줄: u v w
#
# 출력 형식
# - 전파 완료 시간의 최솟값
#
# 제한
# - 2 <= N <= 2*10^5
# - 1 <= M <= 3*10^5
# - 0 <= K <= N
# - 1 <= w <= 10^6
# - 그래프는 모든 정점이 1번에서 도달 가능함
#
# 예시
# 입력
# 5 6 1
# 1 2 2
# 1 3 4
# 2 4 2
# 3 4 1
# 4 5 3
# 2 5 10
#
# 출력
# 8
#
# 설명
# - 중계 서버를 적절히 고르면 일반 서버의 +1초 누적 지연을 줄여 전체 완료 시간을 최소화할 수 있다.

# ============================================================
# 가중치가 있는 노드간 최단 경로 문제로 모델링할 수 있다.
# - 중계 서버는 0초 지연, 일반 서버는 1초 지연으로 생각한다.
# - Dijkstra 알고리즘으로 최단 경로를 구하면 된다.
# ============================================================
import heapq

n = int(input().split()[0])
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


global_min_time = float('inf')
for relay in range(n):
    # relay 서버를 중계 서버로 지정
    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)]  # (시간, 노드)
    
    while pq:
        time, node = heapq.heappop(pq)
        if time > dist[node]:
            continue
        for neighbor, w in graph[node]:
            new_time = time + w + (0 if neighbor == relay else 1)  # relay는 지연 없음
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    global_min_time = min(global_min_time, max(dist))
print(global_min_time)
