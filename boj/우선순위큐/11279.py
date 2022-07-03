import heapq
import sys

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        print(heapq.heappop(nums) * -1 if nums else 0)

    else:
        heapq.heappush(nums, num * -1)
