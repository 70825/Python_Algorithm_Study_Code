n = int(input())
A = set(map(int,input().split()))
A = sorted(list(A))
print(' '.join(map(str,A)))