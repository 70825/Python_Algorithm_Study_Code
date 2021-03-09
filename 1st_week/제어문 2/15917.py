input = __import__('sys').stdin.readline
q = int(input())
for i in range(q):
    a = int(input())
    ans = 0
    while a > 1 and a % 2 == 0:
        a //= 2
    if a == 1: ans = 1
    print(ans)