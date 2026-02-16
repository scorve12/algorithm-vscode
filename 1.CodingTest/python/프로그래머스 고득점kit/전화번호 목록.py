# #전화번호 목록

# def solution(phone_book):
#     answer = True
#     #sort() 함수를 이용하여 전화번호 목록을 정렬한다. 정렬된 전화번호 목록에서 접두어 관계에 있는 전화번호는 인접하게 위치하게 된다.
#     phone_book.sort()
    
#     #정렬된 전화번호 목록에서 인접한 전화번호끼리 비교하여 접두어 관계인지 확인한다.
#     for i in range(len(phone_book) - 1):
#         #startswith() 함수를 이용하여 phone_book[i + 1]이 phone_book[i]로 시작하는지 확인한다. 
#         #만약 phone_book[i + 1]이 phone_book[i]로 시작한다면, answer를 False로 설정하고 반복문을 종료한다.
#         if phone_book[i + 1].startswith(phone_book[i]):
#             answer = False
#             break
#     return answer

def solution(phone_book):
    phone_book.sort()
    
    # p1(현재 번호)과 p2(다음 번호)를 짝지어 비교
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
        
    return True