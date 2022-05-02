from collections import deque

# 괄호의 짝이 맞는지 확인
def isCorrect(s):

    stack = []
    queue = deque(list(s))

    # 모든 문자를 확인할 때 까지
    while queue:

        # 맨 앞부터 문자를 하나씩 확인한다.
        c = queue.popleft()

        # 만약 여는 괄호이거나, 스택에 아무런 값이 존재하지 않을 경우
        if c in "({[" or len(stack) == 0:
            stack.append(c)

        # 스택에 값이 존재하며, 닫는 괄호일 때
        # 각 괄호의 닫는 괄호가 스택의 최상단에 존재하지 않는 경우 -> 짝이 맞지 않는 경우 -> False
        # 짝이 맞다면, 스택에서 해당 여는 괄호를 pop으로 삭제
        else:
            if c == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False

            elif c == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False

            elif c == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False

    # 만약 스택에 남아있는 괄호가 존재할 경우, 짝이 맞지 않는 경우가 존재하는 것 이기 때문에 False
    return True if len(stack) == 0 else False


def solution(s):

    answer = 0

    # 초기 상태 확인 (회전 0번)
    if isCorrect(s):
        answer += 1

    # 길이가 N인 문자는 총 1 ~ N-1번의 회전을 하여 확인한다.
    for _ in range(len(s) - 1):

        # 회전
        s = s[1:] + s[0]

        # 괄호 짝이 맞는지 함수를 사용하여 확인
        # 맞다면 숫자 +1
        if isCorrect(s):
            answer += 1

    return answer


s = "[](){}"
print(solution(s))
