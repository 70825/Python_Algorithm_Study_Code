arr = list()
for i in range(7):
    x = int(input())
    arr.append(x)
sum_odd = 0
min_odd = 101 #입력값이 100이하의 자연수이므로
for i in range(7):
    if arr[i] % 2 == 1:
        sum_odd += arr[i]
        if min_odd > arr[i]:
            min_odd = arr[i]
if min_odd == 101:
    print(-1)
else:
    print(sum_odd)
    print(min_odd)