N = int(input())

fib_answer = 0
fibonacci_answer = 0
fibonacci_info = [0] * (N + 1)


def fib(n):

    global fib_answer

    if n == 1 or n == 2:
        fib_answer += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):

    global fibonacci_answer

    fibonacci_info[1] = 1
    fibonacci_info[2] = 1

    for i in range(3, n + 1):
        fibonacci_answer += 1
        fibonacci_info[i] = fibonacci_info[i - 1] + fibonacci_info[i - 2]

    return fibonacci_info[n]


fib(N)
fibonacci(N)
print(fib_answer, fibonacci_answer)
