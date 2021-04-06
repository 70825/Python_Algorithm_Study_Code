m,n=map(int,input().split())
arr = []
val = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
if m == 0: print(0)
else:
    while m != 0:
        arr.append(val[m % n])
        m //= n
    print(''.join(arr[::-1]))