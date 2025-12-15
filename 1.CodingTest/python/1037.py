#N의 약수가 모두 주면 N을 찾을 수 있는 알고리즘.

N = int(input())
arr = list(map(int, input().split()))

min_A = min(arr)
max_A = max(arr)

#print(min_A)
#print(max_A)

print(max_A * min_A)