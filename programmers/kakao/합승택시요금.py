# 최대 노드 값과 정수형의 이름을 가진 일반적인 그래프일때
# 노드는 1부터 시작
def Floyd_Warshall(n, graph):

    # 각 노드쌍의 최소 거리 정보를 담는 리스트
    info = [[float("inf")] * (n + 1) for _ in range(n + 1)]

    # 각 노드쌍의 초기 거리 정보를 설정
    for start, end, weight in graph:
        info[start][end] = weight
        info[end][start] = weight

    # 모든 노드 쌍 확인, k를 중간 노드로 사용
    for k in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):

                # 출발노드와 도착노드가 같은 경우
                if start == end:
                    info[start][end] = 0
                    continue

                # 중간 노드를 거치는 것과, 그냥 가는것 중 어떤 것이 더 적은 비용이 드는지 확인
                if info[start][k] and info[k][end]:
                    info[start][end] = min(
                        info[start][end], info[start][k] + info[k][end]
                    )

    return info


def solution(n, s, a, b, fares):

    # 최소값을 구하기 위해 answer 초기 값 설정
    answer = float("inf")

    # 플로이드-와샬 알고리즘을 사용하여 각 노드쌍의 최소거리를 구한다.
    result = Floyd_Warshall(n, fares)

    # 완전 탐색을 이용하여, A와 B가 따로 택시를 타게되는 경우의 수를 모두 비교한다.
    for i in range(1, n + 1):
        answer = min(answer, result[s][i] + result[i][a] + result[i][b])

    return answer


n = 6
s = 4
a = 6
b = 2
fares = [
    [4, 1, 10],
    [3, 5, 24],
    [5, 6, 2],
    [3, 1, 41],
    [5, 1, 24],
    [4, 6, 50],
    [2, 4, 66],
    [2, 3, 22],
    [1, 6, 25],
]
print(solution(n, s, a, b, fares))
