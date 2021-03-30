arr = input().split()
ans = []
d = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

for i in range(len(arr)):
    if arr[i] in d:
        if i == 0: ans.append(arr[i])
    else:
        ans.append(arr[i])

res = []
for i in range(len(ans)):
    res.append(ans[i][0].upper())
print(''.join(res))