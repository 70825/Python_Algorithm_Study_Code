t = int(input())
for i in range(t):
    b = int(input())
    s = input()
    ans = []
    for j in range(0,len(s),8):
        x = list(s[j:j+8])
        for k in range(8):
            if x[k] == 'I': x[k] = 1
            else: x[k] = 0
        x = ''.join(map(str,x))
        x = int(x,2)
        ans.append(chr(x))
    print('Case #{}: {}'.format(i+1, ''.join(ans)))