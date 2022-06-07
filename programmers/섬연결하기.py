from collections import defaultdict
import heapq


def solution(n, costs):

    graph = defaultdict(dict)

    # 그래프의 정보를 저장한다.
    for start_node, end_node, weight in costs:
        graph[start_node][end_node] = weight
        graph[end_node][start_node] = weight

    # 노드의 방문 여부를 저장한다.
    visit = {node: False for node in graph}

    start = 0

    # 시작 노드의 방문여부는 True
    visit[start] = True

    # 간선의 정보
    edge_state = []

    # 현재 노드를 시작노드로 설정
    current_node = start

    # 간선의 갯수 저장
    edge = 0

    # 가중치의 합
    answer = 0

    # 정점이 N개일 때 간선이 (N-1) 개가 되기 전까지
    while edge < len(graph) - 1:

        # 현재 노드와 연결된 노드들 확인
        for connect_node in graph[current_node]:

            # 아직 방문하지 않은 연결된 노드의 간선 정보를 최소 힙에 저장
            if visit[connect_node] == False:
                heapq.heappush(edge_state, (graph[current_node][connect_node], connect_node))

        # 간선이 존재하는 경우
        if edge_state:

            # 최소 간선으로 접근 가능한 노드의 정보를 얻어온다.
            while True:
                new_weight, new_node = heapq.heappop(edge_state)

                # 방문하지 않은 노드일 때까지 최소힙에서 계속 pop
                if visit[new_node] == False:
                    break

            # 가중치의 합을 더해준다.
            answer += new_weight

            # 방문한 노드로 설정
            visit[new_node] = True

            # 현재 노드를 새로운 노드로 갱신
            current_node = new_node

            # 간선 증가
            edge += 1

    return answer


test = [
    (5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]], 15),
    (5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]], 8),
    (4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]], 9),
    (5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]], 104),
    (6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]], 11),
    (5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]], 6),
    (5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]], 8),
    (5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]], 8),
    (4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]], 4),
]

for i, case in enumerate(test, start=1):
    n, costs, result = case
    print(f"TEST {i} : {solution(n, costs) == result}")


print(solution(n, costs))
