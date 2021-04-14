n, m = map(int,input().split())
arr = list(list(input()) for _ in range(n))

ans = float('inf')
for i in range(n-7):
    for j in range(m-7):
        white_start = 0
        black_start = 0
        for x in range(8):
            for y in range(8):
                if arr[i+x][j+y] == 'W':
                    if (i+x+j+y) % 2 == 0:black_start += 1
                    else:white_start += 1
                else:
                    if (i+x+j+y) % 2 == 0:white_start += 1
                    else: black_start += 1
        ans = min(ans, white_start, black_start)
print(ans)