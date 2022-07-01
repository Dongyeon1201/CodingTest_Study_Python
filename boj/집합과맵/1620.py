from collections import defaultdict

N, M = map(int, input().split())
pokemons = [input() for _ in range(N)]
questions = [input() for _ in range(M)]

str_info = defaultdict(int)
int_info = [None] * (N + 1)


for i, item in enumerate(pokemons, start=1):
    int_info[i] = item
    str_info[item] = i

for q in questions:
    if str_info[q]:
        print(str_info[q])
    else:
        print(int_info[int(q)])
