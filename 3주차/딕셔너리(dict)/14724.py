D = {'PROBRAIN': 0, 'GROW': 0, 'ARGOS': 0, 'ADMIN': 0, 'ANT': 0, 'MOTION': 0, 'SPG': 0, 'COMON': 0, 'ALMIGHTY': 0}
key = list(D.keys())

n = int(input())
for i in range(len(key)):
    arr = list(map(int,input().split()))
    D[key[i]] = max(arr)

ans = ['', 0] # 동아리 이름, 최대값을 저장할 곳
for i in range(len(key)):
    if D[key[i]] > ans[1]:
        ans[0] = key[i]
        ans[1] = D[key[i]]
print(ans[0])