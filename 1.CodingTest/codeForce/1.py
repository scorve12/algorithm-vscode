# 알파벳에서 연속적인(인접한) 글자들로 구성되어 있고, 각 글자가 정확히 한 번만 나타나는 문자열을 다양한(diverse) 문자열이라고 부릅니다.

# 예를 들어, 다음 문자열들은 다양한 문자열입니다: "fced", "xyz", "r", "dabcef".
# 반면, 다음 문자열들은 다양한 문자열이 아닙니다: "az", "aa", "bad", "babc".
# 참고로 'a'와 'z'는 인접한 글자가 아닙니다.

# 엄밀히 말하면, 문자열에 포함된 모든 글자의 알파벳 위치를 고려했을 때, 이 위치들이 빈틈없이 이어지는 연속적인 구간을 형성해야 합니다. 또한, 문자열 내의 모든 글자는 서로 달라야 합니다(중복 허용 안 됨).

# 여러 개의 문자열이 주어졌을 때, 각 문자열이 다양한 문자열인지 판별하는 프로그램을 작성하세요.

# 입력
# 첫 번째 줄에는 처리할 문자열의 개수를 나타내는 정수 
# n
# n (
# 1
# ≤
# n
# ≤
# 100
# 1≤n≤100)이 주어집니다.

# 다음 
# n
# n개의 줄에는 문자열이 한 줄에 하나씩 주어집니다. 각 문자열은 영어 소문자로만 구성되어 있으며, 길이는 
# 1
# 1 이상 
# 100
# 100 이하입니다.

# 출력
# 입력으로 주어진 각 문자열에 대해 한 줄씩 결과를 출력합니다. 해당 문자열이 다양하다면 "Yes"를, 그렇지 않다면 "No"를 출력하세요. "Yes"와 "No"를 출력할 때 대소문자는 구분하지 않습니다 (예: "YeS", "no", "yES" 모두 허용).

import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = sys.stdin.readline().strip()
    unique_chars = set(s)
    
    if len(unique_chars) != len(s):
        print("No")
        continue
    
    sorted_chars = sorted(unique_chars)
    is_diverse = True
    
    for i in range(1, len(sorted_chars)):
        if ord(sorted_chars[i]) - ord(sorted_chars[i - 1]) != 1:
            is_diverse = False
            break
    
    if is_diverse:
        print("Yes")
    else:
        print("No")