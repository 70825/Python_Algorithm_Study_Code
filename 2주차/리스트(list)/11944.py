N, M = map(int,input().split())
n = list(str(N)) * N
if len(n) > M: print(''.join(n[:M]))
else: print(''.join(n))