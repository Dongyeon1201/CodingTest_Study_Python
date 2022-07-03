import heapq
import sys

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if nums:
            abs_num, real_num = heapq.heappop(nums)
            print(real_num)
        else:
            print(0)

    else:
        heapq.heappush(nums, (abs(num), num))
