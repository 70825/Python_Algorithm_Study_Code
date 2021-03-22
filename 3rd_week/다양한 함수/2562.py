arr = []
for i in range(9):
    x = int(input())
    arr.append(x)
for i in range(9):
    if max(arr) == arr[i]:
        print(max(arr))
        print(i+1)
        exit()