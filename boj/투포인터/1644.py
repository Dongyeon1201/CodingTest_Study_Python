N = int(input())


def get_prime_num_list(n):

    # 0, 1은 False
    info = [False] * 2 + [True] * (n - 1)
    prime_num_list = []

    for i in range(2, n + 1):
        if info[i]:
            prime_num_list.append(i)
        for j in range(i * 2, n + 1, i):
            info[j] = False

    return prime_num_list


info = get_prime_num_list(N)

left = 0
right = 0
sum_num = 0
answer = 0

while True:

    if sum_num == N:
        sum_num -= info[left]
        left += 1
        answer += 1

    if sum_num > N:
        sum_num -= info[left]
        left += 1

    else:
        if right == len(info):
            break

        sum_num += info[right]
        right += 1

print(answer)
