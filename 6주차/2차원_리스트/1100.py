arr = []
for i in range(8):
    arr.append(list(input()))

ans = 0
for i in range(8):
    for j in range(8):
        color = (i + j) % 2
        if color == 0 and arr[i][j] == 'F':
            ans += 1
print(ans)