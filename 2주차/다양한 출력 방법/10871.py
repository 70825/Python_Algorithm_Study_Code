N, X = map(int,input().split())
A = list(map(int,input().split()))
ans = []
for i in range(N):
    if X > A[i]: ans.append(A[i])
print(' '.join(map(str,ans)))