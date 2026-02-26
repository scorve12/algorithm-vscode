import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0] #answer는 딕셔너리 형태로 반환되므로, 키값을 리스트로 변환하여 첫 번째 요소를 반환


test_participant = ["leo", "kiki", "eden"]
test_completion = ["eden", "kiki"]

print(solution(test_participant, test_completion))