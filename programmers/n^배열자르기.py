def solution(n, left, right):

    count = 0
    idx = 1
    array = []

    while count < right:
        if left // n:

            # right 값을 left와의 거리로 변경
            right -= left

            # left가 몇행에 존재하는지 구하기
            line = left // n

            # left가 행의 몇번째 요소인지 확인
            left %= n

            # left의 값을 더해주어 기존에 left와의 차이 값을 사용하여 인덱스로 변경해준다.
            right += left

            # 현재 몇행인지 인덱스 갱신
            idx += line

        else:
            array += ([idx] * idx) + list(range(idx + 1, n + 1))
            count += n
            idx += 1

    return array[left : right + 1]


n = 4
left = 7
right = 14
print(solution(n, left, right))
