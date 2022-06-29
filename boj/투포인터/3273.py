N = int(input())
info = list(map(int, input().split()))
search = int(input())

answer = 0

# 오름차순 정렬
info.sort()

# 투 포인터를 이용
left = 0
right = N - 1

# 두 지점이 만나기 직전까지
while left < right:

    # 합을 줄이기 위해 right를 왼쪽으로 이동
    if info[left] + info[right] > search:
        right -= 1

    # 합을 키우기 위해 left를 오른쪽으로 이동
    elif info[left] + info[right] < search:
        left += 1

    # 같을 경우, left를 오른쪽으로 이동
    # answer += 1
    elif info[left] + info[right] == search:
        answer += 1
        left += 1

print(answer)
