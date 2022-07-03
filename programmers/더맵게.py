import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while scoville:
        x = heapq.heappop(scoville)

        if x >= K:
            return count
        elif scoville == []:
            return -1

        y = heapq.heappop(scoville)

        new_scoville = x + y * 2

        heapq.heappush(scoville, new_scoville)
        count += 1
