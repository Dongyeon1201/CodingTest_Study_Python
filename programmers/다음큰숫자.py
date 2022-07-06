# def solution(n):
#
#     # 모두 1비트인 경우, 가장 상위비트에 0을 추가
#     str_bin = ["0"] + list(str(bin(n))[2:])
#     temp = 0
#
#     # 같은 갯수의 0, 1 비트수를 사용하기 위해 기존 비트를 옮기기만 한다.
#     # 상위비트가 0, 현재 비트가 1일때 위치를 바꿔주며 더 큰 값으로 만든다.
#     for i in range(len(str_bin) - 1, 0, -1):
#         if str_bin[i] == "1" and str_bin[i - 1] == "0":
#             str_bin[i], str_bin[i - 1] = str_bin[i - 1], str_bin[i]
#             temp = i
#             break
#
#     # 더 크게 바뀐 값에서 같은 0, 1 비트수로 값을 최대한 줄이기 위해
#     # 1 비트를 최대한 오른쪽으로 이동한다.
#     idx = len(str_bin) - 1
#     while idx > temp:
#         if str_bin[idx] == "0" and str_bin[idx - 1] == "1":
#             str_bin[idx], str_bin[idx - 1] = str_bin[idx - 1], str_bin[idx]
#
#         idx -= 1
#
#     return int("".join(str_bin), 2)


def solution(n):

    count = bin(n).count("1")

    for num in range(n + 1, 1000001):
        if count == bin(num).count("1"):
            return num


n = 15
print(n, solution(n))
