k, n = map(int,input().split())
k %= 26

s = list(input())
for i in range(n):
    x = ord(s[i])
    if 65 <= x <= 90 or 97 <= x <= 122:
        if s[i].isupper(): x -= 65
        else: x -= 97
        x += k
        x %= 26
        if s[i].islower(): x += 97
        else: x += 65
        s[i] = chr(x)

print(''.join(s))