a = input()
isValid = True
stack = []
for i in range(0, len(a)):
    ch = a[i]
    if(len(stack) == 0):
        stack.append(ch)
    else:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if ch == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    isValid = False
                    break
            if ch == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    isValid = False
                    break
            if ch == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    isValid = False
                    break
print(isValid)