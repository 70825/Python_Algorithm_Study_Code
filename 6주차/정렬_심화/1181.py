n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr = list(set(arr))

arr.sort(key=lambda x: [len(x), x])
print('\n'.join(arr))