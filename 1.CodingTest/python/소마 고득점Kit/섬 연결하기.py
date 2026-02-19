"""
[섬 연결하기] - BFS/DFS + Union-Find (크루스칼)

문제 설명:
n개의 섬 사이에 다리를 건설하려 합니다.
각 다리의 건설 비용이 주어질 때, 모든 섬을 연결하는 최소 비용을 구하세요.

제한사항:
- 섬의 개수 n은 1 이상 100 이하
- costs의 각 원소는 [섬1, 섬2, 비용] 형태
- 같은 연결은 두 번 주어지지 않음
- 모든 섬을 연결할 수 있는 경우만 입력으로 주어짐

입출력 예:
n=4, costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] → 4
"""


def solution(n, costs):
    # 크루스칼 알고리즘 (MST)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # 경로 압축
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    costs.sort(key=lambda x: x[2])  # 비용 기준 정렬
    total = 0
    edges = 0

    for a, b, cost in costs:
        if union(a, b):
            total += cost
            edges += 1
            if edges == n - 1:
                break

    return total


# 테스트
assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
print("섬 연결하기: 모든 테스트 통과!")
