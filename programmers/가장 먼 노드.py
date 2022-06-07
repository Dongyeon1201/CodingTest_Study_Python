from collections import defaultdict, deque


def solution(n, edge):

    # 노드의 연결정보 확인
    connect_info = defaultdict(list)

    # 각 노드에 도달하기 위한 간선 갯수 확인
    edge_count_info = [0] * (n + 1)

    # 각 노드의 방문 여부 확인
    visit = [False] * (n + 1)

    # 시작 노드는 방문 처리
    visit[1] = True

    # 연결 정보 설정
    for start, end in edge:
        connect_info[start].append(end)
        connect_info[end].append(start)

    # (노드, 지나온 간선 갯수) 형태
    state = deque([(1, 0)])

    while state:

        # 노드, 지나온 간선 갯수
        node, count = state.popleft()

        # 간선 갯수를 기록하는 리스트에 기록
        edge_count_info[node] = count

        # 연결된 노드 확인
        for connect_node in connect_info[node]:

            # 연결된 노드 중 방문하지 않은 경우
            if visit[connect_node] == False:

                # 방문해야하는 노드를 큐에 추가
                # 간선 갯수 +1
                state.append((connect_node, count + 1))

                # 해당 노드 방문 처리
                visit[connect_node] = True

    # 간선의 갯수를 저장하는 리스트에서 가장 큰 원소를 가지는 인덱스가 몇개인지 구한다.
    return edge_count_info.count(max(edge_count_info))


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
