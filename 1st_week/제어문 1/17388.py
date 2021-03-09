s,k,h=map(int,input().split())
if s+k+h>99:print('OK')
else:
    Min = s
    if Min > k: Min = k
    if Min > h: Min = h
    if Min == s: print('Soongsil')
    elif Min == k: print('Korea')
    else:print('Hanyang')