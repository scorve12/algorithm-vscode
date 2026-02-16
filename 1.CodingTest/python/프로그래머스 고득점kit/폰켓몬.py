#폰켓몬

def solution(nums):
    answer = 0
    n = len(nums) // 2
    
    #set을 이용하여 중복제거
    s = set(nums)

    #[3, 3, 2, 1] -> {1, 2, 3}

    if len(s) < n:
        answer = len(s)
    else:
        answer = n
    return answer

#def solution(ls):
#    return min(len(ls)/2, len(set(ls)))
# 최소 값을 구하는 방법도 있다.
