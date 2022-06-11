def solution(gems):

    # 투 포인터를 활용하기 위한 시작 index와 끝 index
    start, end = 0, 0

    min_len = float("inf")
    answer = []

    # 각 보석의 갯수
    gem_info = {gem: 0 for gem in set(gems)}

    # 마지막까지 확인
    while end < len(gems):

        # 0부터 마지막까지 탐색하면서 보석 수 확인
        gem_info[gems[end]] += 1
        end += 1

        # 모든 보석이 하나 이상씩 존재할 때
        if all(gem_info.values()):

            while start < end:

                # 시작 위치의 보석이 이미 존재하는 경우
                # 시작 위치를 이동해준다.
                # 최대한 보석수를 줄이는 것
                if gem_info[gems[start]] > 1:
                    gem_info[gems[start]] -= 1
                    start += 1

                # 시작지점 ~ 끝지점 거리가 더 짧아진 경우
                elif end - start < min_len:
                    min_len = end - start
                    answer = [start + 1, end]
                    break

                else:
                    break

    return answer


gems = ["DIA", "EM", "EM", "RUB", "DIA"]
print(solution(gems))
