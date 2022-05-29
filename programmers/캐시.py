from collections import deque


def solution(cacheSize, cities):

    # 총 실행시간
    answer = 0

    # 캐시
    # LFU 사용을 위해 양방향 pop, append가 빠른 deque를 사용
    cache = deque([])

    for city in cities:

        # 대소문자 구분 없이
        city = city.lower()

        # 캐시 히트
        # 해당 데이터를 캐시 최상단으로 올리고, 탐색을 종료
        for i, item in enumerate(cache):
            if item == city:
                del cache[i]
                cache.append(item)
                answer += 1
                break

        # 캐시 미스
        else:
            answer += 5

            # 스택에 도시 추가
            cache.append(city)

            # 가장 오래된 데이터(도시) 제거
            if len(cache) > cacheSize:
                cache.popleft()

    return answer


cacheSize = 5
cities = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "SanFrancisco",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
]
print(solution(cacheSize, cities))
