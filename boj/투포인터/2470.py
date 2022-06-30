N = int(input())
info = list(map(int, input().split()))
info.sort()

left = 0
right = N - 1

min_value = float("inf")
answer = [info[0], info[-1]]

while left < right:

    # 혼합물의 특성값이 이전보다 0에 더 가까울때
    if abs(info[left] + info[right]) <= min_value:
        min_value = abs(info[left] + info[right])
        answer = [info[left], info[right]]

        # 혼합물의 특성값이 0일때 바로 종료
        if min_value == 0:
            break

    # 이동
    if info[left] + info[right] > 0:
        right -= 1
    else:
        left += 1

print(*answer)
