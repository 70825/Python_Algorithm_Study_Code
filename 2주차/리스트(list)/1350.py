n = int(input())
arr = list(map(int,input().split()))
cluster = int(input())
ans = 0
for i in range(len(arr)):
    # 몫과 나머지를 이용하여 ans에 값을 저장함
    # 나머지가 0이면 몫만 곱하고, 나머지가 0이 아니면 cluster 용량이 하나 더 필요하므로 cluster를 더함
    a = arr[i] // cluster # 몫
    b = arr[i] % cluster # 나머지
    ans += cluster * a
    if b != 0: ans += cluster
print(ans)