t = int(input())
for i in range(t):
    s = int(input())
    n = int(input())
    for j in range(n):
        arr = tuple(map(int,input().split()))
        s += arr[0] * arr[1]
    print(s)