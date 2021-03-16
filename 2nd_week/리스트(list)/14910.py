n = list(map(int,input().split()))
flag = True
for i in range(1,len(n)):
    if n[i-1] > n[i]: flag = False
if flag == True: print('Good')
else: print('Bad')