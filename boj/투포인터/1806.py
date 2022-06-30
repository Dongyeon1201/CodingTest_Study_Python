N, S = map(int, input().split())
info = list(map(int, input().split()))

left = 0
right = 0

sum_value = 0
min_value = float("inf")

while True:

    # 이 조건은 반드시 한번씩 실행되야된다.
    if sum_value >= S:

        # 최소 길이 갱신
        if right - left < min_value:
            min_value = right - left

        # 부분 합 갱신
        sum_value -= info[left]

        # 다음 left로
        left += 1

    else:
        # 다음 반복 여부를 여기에 설정한 것이 위 조건을 무조건 한번은 실행하게 하기 위해서이다.
        if right == N:
            break

        # 다음 right로
        sum_value += info[right]
        right += 1

print(min_value if min_value != float("inf") else 0)
