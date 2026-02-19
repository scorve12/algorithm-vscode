"""
[괄호 변환] - 문자열 + 재귀

문제 설명:
'('와 ')'로 이루어진 문자열을 올바른 괄호 문자열로 변환합니다.
다음 알고리즘을 수행합니다:

1. 빈 문자열이면 빈 문자열 반환
2. 문자열을 "균형잡힌 괄호 문자열" u와 나머지 v로 분리
   (u는 균형잡힌 괄호의 최소 접두사)
3. u가 올바른 괄호 문자열이면: u + solution(v) 반환
4. u가 올바르지 않으면:
   - '(' + solution(v) + ')' + (u의 첫/마지막 제거 후 괄호 뒤집기) 반환

제한사항:
- 문자열 길이는 2 이상 1,000 이하 (짝수)
- '('와 ')'의 개수는 항상 같음

입출력 예:
"(()())()" → "(()())()"
")(" → "()"
"()))((()" → "()(())()"
"""


def solution(p):
    if not p:
        return ""

    # u, v 분리 (균형잡힌 최소 접두사)
    count = 0
    for i, ch in enumerate(p):
        count += 1 if ch == '(' else -1
        if count == 0:
            u, v = p[:i + 1], p[i + 1:]
            break

    # u가 올바른 괄호 문자열인지 확인
    if u[0] == '(':
        return u + solution(v)
    else:
        # u의 첫/마지막 제거 후 괄호 뒤집기
        inner = ""
        for ch in u[1:-1]:
            inner += ')' if ch == '(' else '('
        return '(' + solution(v) + ')' + inner


# 테스트
assert solution("(()())()") == "(()())()"
assert solution(")(") == "()"
assert solution("()))((()") == "()(())()"
assert solution("") == ""
print("괄호 변환: 모든 테스트 통과!")
