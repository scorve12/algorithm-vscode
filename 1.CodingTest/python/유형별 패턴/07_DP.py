"""
DP (동적 프로그래밍) 패턴 정리
- 큰 문제를 작은 하위 문제로 분해
- 중복 계산을 저장하여 재사용
- 활용: 최적화, 경우의 수, 문자열 비교
"""
from functools import lru_cache


# ============================================================
# 1. 1D DP - 기본
# ============================================================
# 계단 오르기 (1칸 또는 2칸)
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 공간 최적화 (변수 2개만 사용)
def climb_stairs_opt(n):
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


# ============================================================
# 2. 1D DP - 최대/최소 부분 합
# ============================================================
# 최대 부분 배열 합 (Kadane's Algorithm)
def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# House Robber (인접 집 못 털기)
def rob(nums):
    if len(nums) <= 2:
        return max(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]


# ============================================================
# 3. 2D DP - 격자 경로
# ============================================================
# 좌상단 → 우하단 경로 수 (오른쪽/아래만 이동)
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# 최소 비용 경로
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]


# ============================================================
# 4. 문자열 DP
# ============================================================
# LCS (최장 공통 부분 수열)
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# 편집 거리 (Edit Distance)
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # 삭제
                                    dp[i][j-1],      # 삽입
                                    dp[i-1][j-1])    # 교체
    return dp[m][n]


# ============================================================
# 5. 배낭 문제 (Knapsack)
# ============================================================
# 0/1 배낭
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]  # 안 넣는 경우
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i-1][w - weights[i-1]] + values[i-1])
    return dp[n][capacity]

# 1D 배열로 최적화 (역순 순회)
def knapsack_01_opt(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # 역순!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

# 완전 배낭 (같은 아이템 여러 번 가능)
def knapsack_unbounded(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):  # 정순!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


# ============================================================
# 6. Top-Down (재귀 + 메모이제이션)
# ============================================================
@lru_cache(maxsize=None)
def coin_change(coins_tuple, amount):
    """동전 교환 - 최소 동전 수"""
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    result = float('inf')
    for coin in coins_tuple:
        sub = coin_change(coins_tuple, amount - coin)
        result = min(result, sub + 1)
    return result

# Bottom-Up 버전
def coin_change_bu(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# ============================================================
# 핵심 정리
# ============================================================
# DP 접근법:
# 1. 상태 정의: dp[i]가 무엇을 의미하는지 명확히
# 2. 점화식 세우기: dp[i]를 이전 상태들로 표현
# 3. 초기값 설정: base case
# 4. 순회 방향: 의존 관계에 맞게 (보통 작은 → 큰)
#
# - Top-Down: 재귀 + @lru_cache (구현 쉬움)
# - Bottom-Up: 반복문 + 배열 (보통 더 빠름)
# - 공간 최적화: 이전 행만 필요하면 1D로 줄이기
# - 0/1 배낭은 역순, 완전 배낭은 정순 순회
