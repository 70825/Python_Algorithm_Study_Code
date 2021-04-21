t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    s = list(input())
    for j in range(len(s)):
        x = ord(s[j])-65
        e = (a*x+b)%26
        s[j] = chr(e+65)
    print(''.join(s))