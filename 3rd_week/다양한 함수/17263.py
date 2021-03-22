n = int(input())
A = list(map(int,input().split()))
A.sort()
print(A[len(A)-1]) #혹은 A[-1]