def solution(s):
    stack = []
    s = list(s)

    while s:
        temp = s.pop()

        if temp == ")":
            while s and s[-1] == ")":
                stack.append(s.pop())

            if s == []:
                return False
            else:
                s.pop()

        elif temp == "(":
            if stack == []:
                return False
            else:
                stack.pop()

    return True if stack == [] else False


s = ")))))"
print(solution(s))
