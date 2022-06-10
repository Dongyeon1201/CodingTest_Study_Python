def solution(gems):

    # 투 포인터를 활용하기 위한 시작 index와 끝 index
    start, end = 0, 0

    min_len = float("inf")
    answer = []

    # 각 보석의 갯수
    gem_info = {gem: 0 for gem in set(gems)}

    while end < len(gems):

        gem_info[gems[end]] += 1
        end += 1

        if all(gem_info.values()):
            while start < end:
                if gem_info[gems[start]] > 1:
                    gem_info[gems[start]] -= 1
                    start += 1

                elif end - start < min_len:
                    min_len = end - start
                    answer = [start + 1, end]
                    break

                else:
                    break

    # 진열대는 idx가 1부터 시작하기 때문에 1씩 증가된 start, end를 그대로 반환
    return answer


gems = ["DIA", "EM", "EM", "RUB", "DIA"]
print(solution(gems))
