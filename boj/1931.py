N = int(input())

rooms = []
count = 1       # 무조건 회의 1번은 한다.

for _ in range(N):
    room = tuple(map(int, input().split()))
    rooms.append(room)

# 시작시간 정렬 후, 끝나는 시간 다시 정렬
rooms.sort(key=lambda x:x[0])
rooms.sort(key=lambda x:x[1])

# 가장 처음 가져옴
before = rooms.pop(0)

for room in rooms:

    # 시작시간과 끝나는 시간이 동일
    if room[0] == room[1]: 
        count += 1
        continue
    
    # 더 좁은 범위(시작 시간이 더 늦고, 끝나는 시간은 더 빠른 회의)의 회의가 존재할 때 변경
    elif before[0] < room[1] and before[1] > room[1]:
        before = room
        continue
    
    # 회의가 겹치지 않을 때
    elif not before[1] > room[0]:
        before = room
        count += 1

print(count)