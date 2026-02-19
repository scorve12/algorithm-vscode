"""
[배낭 문제] - DP (0/1 Knapsack)

문제 설명:
배낭의 최대 용량 capacity와 물건들의 [무게, 가치]가 주어질 때,
배낭에 담을 수 있는 물건들의 최대 가치를 구하세요.
각 물건은 하나만 존재합니다.

제한사항:
- 물건의 수는 1 이상 100 이하
- capacity는 1 이상 100,000 이하
- 각 물건의 무게와 가치는 1 이상 1,000 이하

입출력 예:
capacity=7, items=[[6,13],[4,8],[3,6],[5,12]] → 14
"""


def solution(capacity, items):
    n = len(items)
    # 1차원 DP로 공간 최적화
    dp = [0] * (capacity + 1)

    for weight, value in items:
        # 역순으로 순회하여 같은 아이템 중복 사용 방지
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]


# 테스트
assert solution(7, [[6, 13], [4, 8], [3, 6], [5, 12]]) == 14
assert solution(10, [[5, 10], [4, 40], [6, 30], [3, 50]]) == 90
assert solution(0, [[1, 1]]) == 0
assert solution(5, [[6, 100]]) == 0
print("배낭 문제: 모든 테스트 통과!")
