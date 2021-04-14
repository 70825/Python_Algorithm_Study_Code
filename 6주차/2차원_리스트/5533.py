n = int(input())
arr = list(list(map(int,input().split())) for _ in range(n))
ans = [0]*n
for i in range(3):
    for j in range(n):
        flag = True
        for k in range(n):
            if j == k: continue
            if arr[j][i] == arr[k][i]:
                flag = False
        if flag: ans[j] += arr[j][i]
print('\n'.join(map(str,ans)))