# 이진 변환 기능
def convert(s):

    count = 0
    before_s_len = len(s)

    # 0 제거
    s = s.replace("0", "")

    # 제거된 0 길이확인
    count += before_s_len - len(s)

    # 문자열의 길이를 이진수로 변환
    s = format(len(s), "b")

    # 변환된 문자열과 제거된 0의 갯수 반환
    return s, count


def solution(s):

    # 제거된 0의 갯수 누적
    delete_0_count = 0

    # 이진 변환 횟수
    convert_count = 0

    # "1" 문자가 아닐때까지 반복
    while s != "1":

        # 이진 변환 수행
        s, count = convert(s)

        # 제거된 0의 갯수 누적
        delete_0_count += count

        # 이진변환 횟수 증가
        convert_count += 1

    return [convert_count, delete_0_count]


s = "110010101001"
print(solution(s))
