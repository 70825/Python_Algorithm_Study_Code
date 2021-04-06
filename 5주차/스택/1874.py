input = __import__('sys').stdin.readline
n = int(input())
stack = []
num = 0
ans = []
flag = True
for i in range(n):
    x = int(input())
    if len(stack) and stack[-1] == x:
        ans.append('-')
        stack.pop()
    elif x > num:
        for j in range(num,x):
            stack.append(num+1)
            num += 1
            ans.append('+')
        ans.append('-')
        stack.pop()
    else: flag = False
if flag: print('\n'.join(ans))
else: print('NO')