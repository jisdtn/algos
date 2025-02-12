
def isValid(s: str) -> bool:
    stack = []
    closetoopen = {")": "(", "]": "[", "}": "{"}

    for i in s:
        if i in closetoopen:
            if stack and stack[-1] == closetoopen[i]:
                stack.pop()
            else:
                return False
        else: stack.append(i)
    return not stack


if __name__ == '__main__':
    s = "()[]{}"
    print(isValid(s))
