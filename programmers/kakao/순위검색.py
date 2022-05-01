from collections import defaultdict
from itertools import combinations


def lower_bound(nums, target):

    left, right = 0, len(nums)

    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right


def solution(info, query):

    result = []
    info_dic = defaultdict(list)

    for info_item in info:
        temp = info_item.split()
        temp_info_key = temp[:-1]
        temp_info_score = int(temp[-1])

        for i in range(5):
            for combi_item in combinations(temp_info_key, i):
                info_dic["".join(combi_item)].append(temp_info_score)

    # 같은 키 들의 데이터를 오름차순 정렬한다.
    for key in info_dic.keys():
        info_dic[key].sort()

    for query_item in query:
        temp = query_item.split()
        score = int(temp[-1])
        temp = "".join([item for item in temp[:-1] if item != "-" and item != "and"])

        # lower_bound를 사용하여, 요청 쿼리의 스코어보다 크거나 같은 숫자의 갯수를 확인한다.
        lower_num_count = len(info_dic[temp]) - lower_bound(info_dic[temp], score)
        result.append(lower_num_count)

    return result


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]

print(solution(info, query))
