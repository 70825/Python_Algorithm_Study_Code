from itertools import combinations as cb

n,m = map(int,input().split())
arr = list(i for i in range(1,n+1))

ans = 0
for x in cb(arr, m):
    print(' '.join(map(str,x)))