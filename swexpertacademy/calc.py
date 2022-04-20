# https://swexpertacademy.com/main/learn/course/lectureVideoPlayer.do

from collections import deque


# 후위 표기식으로 변경해준다.
def postfix(s):

    # 연산자들의 우선순위를 정한다.
    # 숫자가 낮을수록 높은 우선순위이다.
    operation_rank = {"*": 1, "/": 1, "+": 2, "-": 2, "(": 3}

    # 연산자가 추가되는 스택이다.
    operation_stack = []

    # 식을 후위표기식으로 변경한 결과가 담긴다.
    after_stack = []

    s = deque(s)

    while s:

        # 맨 앞부터 하나씩 확인한다.
        item = s.popleft()

        # 1. 숫자는 바로 추가
        if item.isdigit():
            after_stack.append(item)

        # 2. ( 도 바로 추가
        elif item == "(":
            operation_stack.append(item)

        # 3. ) 는 닫는 괄호가 나올때까지 연산자 스택에서 pop하여 후위표기식에 추가
        elif item == ")":
            while operation_stack[-1] != "(":
                after_stack.append(operation_stack.pop())

            # top의 '(' 제거
            operation_stack.pop()

        # 연산자 스택이 빈 상태가 아닐 경우
        # 현재 뽑은 연산자 순위보다 높거나 같은 연산자들을 추가 (계산도 높은 우선순위 연산자를 먼저 하기 때문)
        else:
            while operation_stack and operation_rank[item] >= operation_rank[operation_stack[-1]]:
                after_stack.append(operation_stack.pop())

            # 이후 현재 연산자 추가
            operation_stack.append(item)

    # 5. 남은거 모두 pop 후 추가
    while operation_stack:
        after_stack.append(operation_stack.pop())

    return after_stack


# 후위 표기식으로 표시된 계산식을 계산한다.
def calc(s):

    # 계산을 위한 스택이다.
    result = []

    # 큐를 사용하여 앞에서부터 확인
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

    return result.pop()


# s = "(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)"
s = "1+2+(3+4)*5"
after = postfix(s)
print(after)
print(calc(after))
