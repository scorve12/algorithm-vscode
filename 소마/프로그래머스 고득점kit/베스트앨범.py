from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # 1. 데이터를 한 번에 정리 (장르별 총 재생수, 곡 정보)
    # defaultdict(int) : 딕셔너리의 기본값을 0으로 설정하여 키가 존재하지 않을 때 자동으로 0을 반환하도록 하는 클래스
    genre_play_count = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_play_count[g] += p # 장르별 총 재생수 누적
        genre_songs[g].append((i, p)) # 장르별 곡 정보 (인덱스, 재생수) 저장

    # 2. 많이 재생된 장르 순으로 정렬
    sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)

    # 3. 각 장르 내에서 정렬 후 최대 2개 추출
    for g in sorted_genres:
        # 재생 횟수(p) 내림차순, 같다면 인덱스(i) 오름차순
        songs = sorted(genre_songs[g], key=lambda x: (-x[1], x[0]))
        answer.extend([s[0] for s in songs[:2]])

    return answer