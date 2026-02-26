#코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

# 예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
# 코니는 하루에 최소 한 개의 의상은 입습니다.
# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
import sys
from : import defaultdict

def solution(clothes):
    # defaultdict: 키가 존재하지 않을 때 자동으로 초기값을 생성하는 딕셔너리
    # defaultdict를 사용해서 카테고리별 의상 개수를 세는 딕셔너리를 만듭니다. 키는 의상 종류(예: "headgear", "eyewear")이고, 값은 해당 종류의 의상 개수입니다.
    category_count = defaultdict(int)
    print(category_count)  # defaultdict(<class 'int'>, {})
    
    # clothes 딕셔너리에는 키[item], 값[category]
    for item, category in clothes:
        category_count[category] += 1 #카테고리 계수만 체크
    
    combinations = 1
    for count in category_count.values(): # 각 카테고리별 의상 개수를 가져와서 조합의 수를 계산합니다. 각 카테고리에서 의상을 입지 않는 경우도 포함하기 위해 (count + 1)을 곱합니다.
        combinations *= (count + 1)  # 각 카테고리에서 의상을 입지 않는 경우도 포함
    
    return combinations - 1  # 모든 카테고리에서 의상을 입지 않는 경우 제외

#이것은 조합 문제 이다.
#조합: n개의 아이템에서 r개를 선택하는 방법의 수
# 예시 입력
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))  # 5

    