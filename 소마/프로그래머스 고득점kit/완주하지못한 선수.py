#완주하지 못한 선수
import collections


def solution(participant, completion):
    #collections.Counter() : 리스트의 요소를 딕셔너리 형태로 {요소: 개수}로 반환하는 함수
    answer = collections.Counter(participant) - collections.Counter(completion)
    dump = collections.Counter(participant) + collections.Counter(completion)

    print(collections.Counter(participant)) #Counter({'mislav': 1, 'stanko': 1, 'ana': 1}
    print(collections.Counter(completion)) #Counter({'stanko': 1, 'ana': 1}
    print(answer) #Counter({'mislav': 1})
    print(dump) #Counter({'mislav': 2, 'stanko': 2, 'ana': 2}
    #answer = {'mislav': 1, 'stanko': 1, 'ana': 1} - {'stanko': 1, 'ana': 1} -> {'mislav': 1}
    # -연산을 통해 participant에서 completion에 있는 요소들을 제거하고 남은 요소가 완주하지 못한 선수이다.
    # [0]은 딕셔너리의 첫번째 요소 즉 완주하지 못한 선수의 이름을 반환한다.
    # anser.keys() -> {'mislav': 1}
    # list(answer.keys()) -> ['mislav']
    # list(answer.keys())[0] -> 'mislav'
    return list(answer.keys())[0]



solution(["mislav", "stanko", "ana"], ["stanko", "ana"])