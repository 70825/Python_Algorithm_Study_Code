n, k = map(int,input().split())
arr1 = list(map(int,input().split(',')))
for i in range(k):
    arr2 = []
    for j in range(1, len(arr1)):
        arr2.append(arr1[j] - arr1[j-1])
    arr1 = arr2
print(','.join(map(str,arr1)))