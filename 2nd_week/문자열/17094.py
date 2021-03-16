n = int(input())
s = input()
a, b = 0, 0 # a = 2의 개수, b = e의 개수
for i in range(n):
    if s[i] == '2': a += 1
    else: b += 1
if a > b: print(2)
elif b > a:print('e')
else: print('yee')