t = int(input())
for i in range(t):
    s = input()
    x = int(s)
    y = int(s[::-1])
    z = str(x+y)

    flag = True
    for j in range(len(z)//2):
        if z[j] != z[-1-j]:
            flag = False

    if flag:print('YES')
    else:print('NO')