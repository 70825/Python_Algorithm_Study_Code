A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())
while not(A2 <= 0 or B2 <= 0):
    A2 -= B1
    B2 -= A1
if A2 <= 0 and B2 <= 0:
    print('DRAW')
elif A2 <= 0:
    print('PLAYER B')
else:
    print('PLAYER A')