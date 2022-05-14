from collections import defaultdict, deque
from email.policy import default
from itertools import count


def solution(N, road, K):

    road_dict = defaultdict(list)

    for a, b, c in road:
        road_dict[a].append((b, c, 0))
        road_dict[b].append((a, c, 0))

    queue = deque(road_dict[1])
    visit = [False] * N+1
    visit[1] = True

    while queue:
        x,  = queue.popleft()

        if visit[x[0]] == False and 

N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
print(solution(N, road, K))
