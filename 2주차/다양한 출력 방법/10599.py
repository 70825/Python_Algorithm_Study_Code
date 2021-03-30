while True:
    arr = list(map(int,input().split()))
    if arr == [0]*4: break
    ans = [arr[2]-arr[1],arr[3]-arr[0]]
    print(' '.join(map(str,ans)))