arr = []
k = int(input())
for i in range(k):
    x = int(input())
    if x != 0: arr.append(x)
    else: arr.pop()
ans = 0
for i in range(len(arr)):
    ans += arr[i]
print(ans)