n = int(input())
arr = tuple(map(int,input().split()))
ans = 0
for i in range(len(arr)):
    if arr[i] != i+1:
        ans += 1
print(ans)