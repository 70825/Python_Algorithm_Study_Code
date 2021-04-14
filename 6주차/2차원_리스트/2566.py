arr = list(list(map(int,input().split())) for _ in range(9))
res = [0, 0, 0]
for i in range(9):
    for j in range(9):
        if arr[i][j] > res[0]:
            res = [arr[i][j], i+1, j+1]
print(res[0])
print(res[1],res[2])