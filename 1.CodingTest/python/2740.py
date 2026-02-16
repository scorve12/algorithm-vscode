import sys

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

M_check, K = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(M)]

C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(*(row))

#입력 예시
#3 2
# 2 3
# N = 3, M = 2, K = 3

#1(<-시작) 2
#3        4            -1(<-시작)  -2   0
#5        6             0         0    3


# (1*-1 + 2*0) (1*-2 + 2*0) (1*0 + 2*3)
# (3*-1 + 4*0) (3*-2 + 4*0) (3*0 + 4*3)
# (5*-1 + 6*0) (5*-2 + 6*0) (5*0 + 6*3)
# -1 -2 6
# -3 -6 12
# -5 -10 18