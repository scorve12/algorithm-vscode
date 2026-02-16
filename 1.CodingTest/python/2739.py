import sys

n = int(input())

for i in range(1,10):
    #str을 사용하여 문자열로 변환을 해야함
    #print(str(n) + " * " + str(i) + " = " + str(n*i))
    print(f"{n} * {i} = {n*i}")

print('\n'.join(f"{n} * {i} = {n * i}" for i in range(1, 10)))