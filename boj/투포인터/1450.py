# 출처 : https://wch18735.github.io/algorithm/Meet_in_the_Middle/#3-%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89%EC%9D%84-%ED%86%B5%ED%95%9C-%EC%A1%B0%EA%B1%B4%EC%97%90-%EB%A7%9E%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EA%B2%80%EC%83%89
from itertools import combinations

N, C = map(int, input().split())
info = list(map(int, input().split()))

answer = 0

# 모든 물건을 반으로 분리
# 2^N -> 2 * 2^(N/2)로 만들기 위함
list_a = info[: N // 2]
list_b = info[N // 2 :]

# 반으로 나눈 첫번째 배열의 모든 물건의 합계 경우의 수를 저장
# 합계가 동일하더라도, 다른 물건이기 때문에 다른 경우로 생각
info_a = []

# 반으로 나눈 두번째 배열의 모든 물건의 합계 경우의 수를 저장
# 합계가 동일하더라도, 다른 물건이기 때문에 다른 경우로 생각
info_b = []

# 첫번째 배열의 각 경우의 모든 조합을 구한 후, 합계를 추가
for i in range(len(list_a) + 1):
    for item in combinations(list_a, i):
        info_a.append(sum(item))

# 두번째 배열의 각 경우의 모든 조합을 구한 후, 합계를 추가
for i in range(len(list_b) + 1):
    for item in combinations(list_b, i):
        info_b.append(sum(item))

# 첫 번째 배열을 이진 탐색하기 위해 정렬
info_a.sort()

# 두 번째 배열은 정렬 없이 각 경우 모두 확인
for item in info_b:

    # 이미 배낭의 한계를 넘은 경우
    if item > C:
        continue

    # 이진 탐색을 위한 포인터
    left = 0

    # 첫번째 배열의 모든경우 마지막 위치
    right = len(info_a)

    # 이진 탐색을 통해 두 번째 배열의 합계 item이 첫번째 배열의 item과 합했을 때, 가장 C과 근접한 경우를 구할 수 있다.
    while left < right:

        mid = (right + left) // 2

        if item + info_a[mid] > C:
            right = mid
        else:
            left = mid + 1

    # 모든 경우의 갯수 누적
    answer += right

print(answer)
