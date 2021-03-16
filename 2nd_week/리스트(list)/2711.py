t = int(input())
for i in range(t):
    arr = input().split()
    idx, D = int(arr[0]), arr[1]
    print(D[:idx - 1] + D[idx:])