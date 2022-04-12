# https://swexpertacademy.com/main/learn/course/lectureVideoPlayer.do

from collections import deque


def solution(s):
    operation_rank = {"*": 1, "/": 1, "+": 2, "-": 2, "(": 3}

    operation_stack = []
    after_stack = []

    s = deque(s)

    while s:
        item = s.popleft()

        # 1. 숫자는 바로 추가
        if item.isdigit():
            after_stack.append(item)
        # 2. ( 도 바로 추가
        elif item == "(":
            operation_stack.append(item)
        # 3. ) 는 닫는 괄호가 나올때까지 pop하여 추가
        elif item == ")":
            while operation_stack[-1] != "(":
                after_stack.append(operation_stack.pop())

            # top의 ( 제거
            operation_stack.pop()

        # 4. 나머지 연산자들은 뽑은 연산자가 더 높은 우선순위가 될때까지 pop하여 추가 -> 이후 뽑은 값 push
        else:
            while operation_rank[item] >= operation_rank[operation_stack[-1]]:
                after_stack.append(operation_stack.pop())

            operation_stack.append(item)

    # 5. 남은거 모두 pop 후 추가
    while operation_stack:
        after_stack.append(operation_stack.popleft())

    return after_stack


def calc(s):
    result = []

    s = deque(s)

    while s:
        item = s.popleft()

        if item.isdigit():
            result.append(int(item))
        else:
            num1 = result.pop()
            num2 = result.pop()

            if item == "+":
                result.append(num2 + num1)
            elif item == "-":
                result.append(num2 - num1)
            elif item == "*":
                result.append(num2 * num1)
            elif item == "/":
                result.append(num2 / num1)

    return result


s = "(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)"
print(calc(solution(s)))
