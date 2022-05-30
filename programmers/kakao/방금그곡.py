# from datetime import datetime

# # 음표가 붙은 음은 소문자로 변환
# def convert_shap(s):
#     return s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")


# def solution(m, musicinfos):

#     # m의 샾이 붙은 음은 소문자로 표현
#     m = convert_shap(m)

#     answer = "(None)"
#     max_time = float("-inf")

#     for item in musicinfos:
#         start, end, music_name, music_info = item.split(",")

#         # 음악시간(분)
#         music_time = (datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")).seconds // 60

#         # 노래의 샾이 붙은 음은 소문자로 표현
#         music_info = convert_shap(music_info)

#         # 반복부분 + 시간 초과로 잘리는 부분
#         music_all = music_info * (music_time // len(music_info)) + music_info[: music_time % len(music_info)]

#         # 찾는음이 그대로 들어있는 경우
#         if m in music_all:

#             # 찾는 음악 중 가장 긴 곡일 때 갱신
#             if max_time < music_time:
#                 answer = music_name
#                 max_time = music_time

#         # 맨 앞, 맨 뒤로 잘려 들어있는 경우 확인
#         else:
#             for i in range(1, len(m)):

#                 # 가장 앞, 가장 뒤 부분으로 나누어 확인
#                 first, last = m[i:], m[:i]

#                 # 전체 음악의 맨 앞, 맨 뒤 부분을 확인
#                 if music_all[: len(m) - i] == first and music_all[len(music_all) - i :] == last:

#                     # 찾는 음악 중 가장 긴 곡일 때 갱신
#                     if max_time < music_time:
#                         answer = music_name
#                         max_time = music_time

#                     break

#     # 음악을 못 찾을 경우
#     return answer


from datetime import datetime

# 음표가 붙은 음은 소문자로 변환
def convert_shap(s):
    return s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")


def solution(m, musicinfos):

    # m의 샾이 붙은 음은 소문자로 표현
    m = convert_shap(m)

    # 일치하는 음악 목록
    answer = []

    musicinfos.sort()

    for i, item in enumerate(musicinfos):
        start, end, music_name, music_info = item.split(",")

        # 음악시간(분)
        music_time = (datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")).seconds // 60

        # 노래의 샾이 붙은 음은 소문자로 표현
        music_info = convert_shap(music_info)

        # 반복부분 + 시간 초과로 잘리는 부분
        music_all = music_info * (music_time // len(music_info)) + music_info[: music_time % len(music_info)]

        # 찾는음이 그대로 들어있는 경우
        if m in music_all:
            answer.append((music_name, music_time, i))

        # 맨 앞, 맨 뒤로 잘려 들어있는 경우 확인
        else:
            for i in range(1, len(m)):

                # 가장 앞, 가장 뒤 부분으로 나누어 확인
                first, last = m[i:], m[:i]

                # 전체 음악의 맨 앞, 맨 뒤 부분을 확인
                if music_all[: len(m) - i] == first and music_all[len(music_all) - i :] == last:
                    answer.append((music_name, music_time, i))
                    break

    # 음악을 못 찾을 경우
    if len(answer) < 1:
        return "(None)"
    else:
        answer.sort(key=lambda x: (-x[1], x[2]))
        return answer[0][0]


m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

print(solution(m, musicinfos))
