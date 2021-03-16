n = int(input())
for i in range(n):
    arr = list(input().split())
    print(' '.join(arr[2::]),arr[0],arr[1])