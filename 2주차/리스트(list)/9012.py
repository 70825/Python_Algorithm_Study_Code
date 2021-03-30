t = int(input())
for i in range(t):
    s = input()
    l, r = 0, 0
    arr = []
    flag = True
    for j in range(len(s)):
        if s[j] == '(':
            l += 1
            arr.append('(')
        else:
            r += 1
            if len(arr) == 0:
                flag = False
            else:
                arr.pop()
    if l == r and flag == True: print('YES')
    else: print('NO')