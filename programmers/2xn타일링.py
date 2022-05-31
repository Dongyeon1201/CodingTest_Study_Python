from collections import defaultdict
import sys

fibonacci_info = defaultdict(int)
sys.setrecursionlimit(10**6)


def solution(n):

    global fibonacci_info

    if fibonacci_info[n] == 0:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            fibonacci_info[n] = (solution(n - 1) + solution(n - 2)) % 1000000007

    return fibonacci_info[n]


n = 11111
a = solution(n)
