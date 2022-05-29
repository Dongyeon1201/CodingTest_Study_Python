from collections import defaultdict, deque

# 그래프의 노드 갯수를 구하는 함수
# 노드의 최대 정점 값, 그래프, 시작 노드를 인자로 받는다.
# 노드의 최대 정점 값 -> visit에 사용
# 시작 노드 -> 순회 시작 부분에 사용
def get_node_count(n, graph, start_node):

    connect_info = defaultdict(list)
    node_count = 0

    for start, end in graph:
        connect_info[start].append(end)
        connect_info[end].append(start)

    visit = [False] * (n + 1)
    state = deque(connect_info[start_node])

    while state:
        for _ in range(len(state)):
            node = state.popleft()

            if visit[node] == False:
                state.extend(connect_info[node])
                visit[node] = True
                node_count += 1

    # node_count가 0이면 연결된 정점이 없는 것이기 때문에 1 반환
    return node_count if node_count > 0 else 1


def solution(n, wires):

    min_difference_count = float("inf")

    for i, item in enumerate(wires):

        # 끊어진 선으로 연결된 두 노드로 그래프가 나뉘어지기 때문에
        # 해당 연결선이 존재하지 않는 그래프를 두 노드로 각각 조회하면, 나뉜 두 그래프를 각각 순회할 수 있다.
        # 즉, 끊어진 두 그래프를 구분하는 방법은 끊어지기 전 연결되었던 두 노드를 이용하면 된다.
        node1, node2 = item

        # 첫번째 그래프의 노드 갯수를 확인
        node1_include_count = get_node_count(n, wires[:i] + wires[i + 1 :], node1)

        # 두번째 그래프의 노드 갯수를 확인
        node2_include_count = get_node_count(n, wires[:i] + wires[i + 1 :], node2)

        # 차이값이 가장 적을 경우
        if abs(node1_include_count - node2_include_count) < min_difference_count:

            # 갱신
            min_difference_count = abs(node1_include_count - node2_include_count)

    return min_difference_count


n = 9
wires = [[1, 2], [2, 3]]
print(solution(n, wires))
