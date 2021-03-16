A = list(map(int,input().split()))
B = list(map(int,input().split()))
a, b = 0, 0
for i in range(10):
    if A[i] > B[i]: a += 3
    elif A[i] < B[i]: b += 3
    else:
        a += 1
        b += 1
print(a, b)
if a > b: print('A')
elif a < b: print('B')
else: print('D')