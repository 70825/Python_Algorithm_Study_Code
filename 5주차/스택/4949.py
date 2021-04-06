while True:
    s = input()
    if s == '.': break
    stack = []
    flag = True
    for i in range(len(s)):
        if s[i] in ['(','[']: stack.append(s[i])
        if s[i] == ')':
            if len(stack) and stack[-1] == '(': stack.pop()
            else: flag = False
        if s[i] == ']':
            if len(stack) and stack[-1] == '[': stack.pop()
            else: flag = False
    if flag and len(stack) == 0: print('yes')
    else: print('no')