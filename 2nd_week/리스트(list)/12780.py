h = list(input())
n = list(input())
ans = 0
for i in range(len(h)):
    if h[i:i+len(n)] == n:
        ans += 1
print(ans)