from collections import deque


def solution(tickets):

    # 모든 방법을 담는 리스트
    result = []

    def dfs(start, other_tickets, route):

        # 더 이상 남은 경로가 없을 때
        if len(other_tickets) < 1:

            # 경로 모음에 출력
            result.append(route)
            return

        # 현재 남은 모든 경로 확인
        for _ in range(len(other_tickets)):

            start_airport, end_airport = other_tickets.popleft()

            # 시작지가 동일한 경로 확인
            if start_airport == start:

                # 새로운 탐색에 새로운 출발지를 현재 경로의 도착지로 설정
                # 방문 공항 목록에 현재 도착지 추가
                dfs(end_airport, other_tickets, route + [end_airport])

            # 현재 단계에서 다른 경로를 탐색하기 위해 다시 추가
            other_tickets.append([start_airport, end_airport])

    # 첫 시작은 "ICN", 방문한 공항 목록에도 "ICN" 추가 후 동작
    dfs("ICN", deque(tickets), ["ICN"])

    # 경로를 알파벳순으로 정렬
    result.sort()

    # 알파벳 순서가 가장 앞서는 경로 반환
    return result[0]


# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
print(solution(tickets))
