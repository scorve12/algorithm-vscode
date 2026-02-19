"""
[최소 편집 거리] - DP (Edit Distance)

문제 설명:
두 문자열 str1, str2가 주어질 때, str1을 str2로 변환하기 위한
최소 편집 연산(삽입, 삭제, 교체) 횟수를 구하세요.

제한사항:
- 각 문자열의 길이는 1 이상 1,000 이하
- 문자열은 소문자 알파벳으로만 구성

입출력 예:
"kitten", "sitting" → 3  (k→s, e→i, 삽입 g)
"sunday", "saturday" → 3  (삽입 a, 삽입 t, n→r)
"""


def solution(str1, str2):
    n, m = len(str1), len(str2)
    # dp[i][j] = str1[:i]를 str2[:j]로 변환하는 최소 연산 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i  # 삭제만으로 변환
    for j in range(m + 1):
        dp[0][j] = j  # 삽입만으로 변환

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # 삭제
                    dp[i][j - 1],      # 삽입
                    dp[i - 1][j - 1],  # 교체
                )

    return dp[n][m]


# 테스트
assert solution("kitten", "sitting") == 3
assert solution("sunday", "saturday") == 3
assert solution("", "abc") == 3
assert solution("abc", "abc") == 0
print("최소 편집 거리: 모든 테스트 통과!")
