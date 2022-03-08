import math

M, N = map(int, input().split())

# 소수 체크 함수
def is_prime(n):
    if n == 1:
        return False
    else:
				
		# 2 ~ N 제곱근(실수 연산을 막기 위해 int형으로 변환) 까지
        for i in range(2,int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    
    return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)