def solution(routes):
    answer = 0

    # 경로를 도달하는 순서로 일렬로 정렬한다.
    # 그 중에서도 최대한 경로의 길이가 짧은 경로를 우선으로 둔다.
    routes.sort(key=lambda x: x[1])

    camera = float("-inf")
    answer = 0

    for start, end in routes:

        # 마지막으로 카메라를 설치한 위치가 새로운 경로의 출발 위치에 도달하지 못했을 때
        if camera < start:

            # 최대한 많이 겹치도록 해당 경로의 마지막 부분에 카메라 설정
            camera = end

            # 카메라 갯수 +1
            answer += 1

    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
# routes = [[-4, -3], [-2, -1], [0, 1]]
print(solution(routes))
