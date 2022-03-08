from collections import deque
import copy

# DFS 함수
def dfs(graph, v, visit):

    # 저장여부를 저장하는 visit에서 방문 노드의 값을 True로 설정
    visit[v] = True

    # 방문한 노드 값 출력
    print(v, end=' ')

    # 그래프의 연결된 관계 확인
    for item in graph:

        # 최상단 노드는 확인하지 않는다.
        if item == []: continue

        else:
            for i in item:

                # 만약 방문한 노드와 연결된 노드가 방문하지 않은 상태일 때
                # dfs 함수를 동작하기전에 낮은 값의 노드를 우선으로 가져오도록 정렬하였다.
                # 노드 방문 순서는 걱정하지 않아도 된다.
                if v in item and visit[i] != True:

                    # 해당 노드를 바로 방문하여 연결된 노드가 존재하는지 확인
                    # 재귀 함수 동작
                    dfs(graph, i, visit)

# BFS 함수
def bfs(graph, v, visit):

    # 시작하는 노드가 들어간 큐를 생성한다.
    queue = deque([v])

    # 첫 방문 노드의 방문 여부를 True로 변경한다.
    visit[v] = True

    # 첫 방문한 노드를 출력한다.
    print(v, end=' ')

    # 큐가 빈 상태가 될 때까지 동작한다.
    # 한 번 반복할 때 마다, 방문한 한 노드의 방문하지 않는 모든 노드가 큐에 삽입된다.
    while queue:

        # 큐에 가장 먼저 삽입된 노드 값을 출력한다.
        # EX) 이전에 (3, 1) (3, 4) 관계에서 3을 확인한 후, 큐에 [1, 4] 가 들어갔다면
        # 이후에는 1과 연결된 노드를 확인하기 위해 1을 꺼내어 확인한다.
        v = queue.popleft()

        for item in graph:
            if item == []: continue
            else:
                i = item[1]

                # 현재 노드와 연결되있으며, 방문하지 않는 노드일 때
                if v == item[0] and visit[i] != True:

                    # 방문한 상태로 변경
                    visit[i] = True

                    # 해당 노드 출력
                    print(i, end=' ')

                    # 다음 while문 동작 시, 해당 노드와 연결된 다른 노드를 확인하기 위해 값 저장
                    # 큐에 순서대로 저장된다.
                    queue.append(i)
                    
# 정점 갯수
N, M, V = map(int, input().split())

# 그래프의 연결된 관계를 나타낸 배열
graph = []

# 각 노드의 간선으로 연결된 관계를 양방향으로 추가해준다.
for _ in range(M):
    x, y = map(int, input().split())
    graph.append([x, y])
    graph.append([y, x])

# 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하기 때문에, 정렬을 해준다.
graph.sort(key=lambda x:[x[0], x[1]])

# 방문 여부를 각 노드의 값으로 확인하기 위해 dict 형태로 저장한다. 
visit = {item: False for i in graph for item in i}

# dfs 함수에서 그래프 초기값을 새로운 변수에 가져온다.
dfs_graph = copy.deepcopy(graph)

# 최상단 노드 추가(배열은 0부터 시작하기 때문에)
dfs_graph.insert(0, [])

# dfs 함수에서 visit 여부를 저장하는 초기값을 새로운 변수에 가져온다.
dfs_visit = copy.deepcopy(visit)

# dfs 함수를 동작
dfs(dfs_graph, V, dfs_visit)

# 한 줄 띄우기
print("")

# bfs 함수에서 그래프 초기값을 새로운 변수에 가져온다.
bfs_graph = copy.deepcopy(graph)

# 최상단 노드 추가(배열은 0부터 시작하기 때문에)
bfs_graph.insert(0, [])

# bfs 함수에서 visit 여부를 저장하는 초기값을 새로운 변수에 가져온다.
bfs_visit = copy.deepcopy(visit)

# bfs 함수 동작
bfs(bfs_graph, V, bfs_visit)