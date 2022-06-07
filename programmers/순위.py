def solution(n, results):
    answer = 0
    graph = [["?"] * (n + 1) for _ in range(n + 1)]

    for i, j in results:
        graph[i][j] = "win"
        graph[j][i] = "lose"

    # i와 j사이의 거쳐가는 노드를 설정 (플로이드-워셜 알고리즘)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):

                # 현재 노드일 경우
                if i == j:
                    graph[i][j] = "-"
                    continue

                # J(승)/K(패) and K(승)/I(패) -> J(승)/I(패) 로 확인할 수 있다.
                if graph[k][i] == "win" and graph[j][k] == "win":
                    graph[j][i] = "win"
                    graph[i][j] = "lose"

    # 0번 노드는 존재하지 않기 때문에, 0번 노드의 정보는 확인하지 않는다.
    for i in graph[1:]:

        # 순위를 알 수 없는 결과가 없을 경우
        if "?" not in i[1:]:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
