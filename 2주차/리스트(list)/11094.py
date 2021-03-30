t = int(input())
S = list('Simon says')
for i in range(t):
    arr = list(input())
    if arr[:10] == S:
        print(''.join(arr[10:]))