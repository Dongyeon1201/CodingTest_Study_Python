def convert(num, k):
    result = ""

    while num // k != 0:
        result += str(num % k)
        num //= k

    result += str(num % k)

    return result[::-1]


def isPrime(num):

    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def solution(n, k):

    answer = 0

    for item in convert(n, k).split("0"):
        if item != "" and isPrime(int(item)):
            answer += 1

    return answer


n = 110011
k = 10

print(solution(n, k))
