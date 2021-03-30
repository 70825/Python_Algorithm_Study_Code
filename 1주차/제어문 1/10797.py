k = int(input())
a,b,c,d,e = map(int,input().split())
ans = 0
if k == a: ans += 1
if k == b: ans += 1
if k == c: ans += 1
if k == d: ans += 1
if k == e: ans += 1
print(ans)