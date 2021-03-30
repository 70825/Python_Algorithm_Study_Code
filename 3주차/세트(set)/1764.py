n, m = map(int,input().split())
A, B = set(),set()
for i in range(n):
    s = input()
    A.add(s)
for i in range(m):
    s = input()
    B.add(s)
C = sorted(list(A & B))
print(len(C))
for i in range(len(C)):
    print(C[i])