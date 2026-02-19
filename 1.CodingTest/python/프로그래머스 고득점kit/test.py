import sys
from collections import defaultdict

def solution(clothes):
    category_count = defaultdict(int)
    
    for item, category in clothes:
        category_count[category] += 1
    
    collaborations = 1
    
    for count in category_count.values():
        collaborations *= (count + 1)
        
    return collaborations - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))  # 5