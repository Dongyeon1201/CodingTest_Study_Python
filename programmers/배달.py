def dijkstra(graph, start):

    # 시작 노드로부터 최소 거리를 저장함
    distances = {node: float("inf") for node in graph}

    # 시작 노드는 값 0
    distances[start] = 0

    # 정점 갯수(출발노드는 이미 0 값이 설정)
    for i in range(len(graph) - 1):

        # 각 노드 확인
        for current_node in graph:

            # 해당 노드와 연결된 노드들 확인
            for connect_node in graph[current_node]:

                # (시작노드 -> 연결노드까지의 거리) > (시작노드 -> 현재노드까지의 거리 + 현재 노드 -> 연결노드까지의 거리)
                if distances[connect_node] > distances[current_node] + graph[current_node][connect_node]:

                    # 갱신
                    distances[connect_node] = distances[current_node] + graph[current_node][connect_node]

    return distances


def solution(N, road, K):

    graph = {i: {} for i in range(1, N + 1)}

    road.sort(key=lambda x: -x[2])

    for start, end, time in road:
        graph[start][end] = time
        graph[end][start] = time

    return len([item for item in dijkstra(graph, 1).values() if item <= K])


N = 6
road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
K = 4
print(solution(N, road, K))
