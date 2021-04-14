arr = list(list(input()) for _ in range(5))

max_len = 0
for i in range(5):
    max_len = max(max_len, len(arr[i]))

for i in range(max_len):
    for j in range(5):
        if len(arr[j]) < i+1: continue
        print(arr[j][i],end='')