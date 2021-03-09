n = int(input())
a, b = 0, 0 #아래 칸, 윗 칸
ans = 0
while not(a == n and b == n):
    if a > b:
        b += 1
    else:
        a += 1
        b = 0
    ans += a + b
print(ans)