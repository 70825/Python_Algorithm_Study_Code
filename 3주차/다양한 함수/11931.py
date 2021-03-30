n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
arr = sorted(arr, reverse = True) # 또는 arr = sorted(arr)[::-1]을 사용
for i in range(n):
    print(arr[i])