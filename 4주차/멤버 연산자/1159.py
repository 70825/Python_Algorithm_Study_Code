n = int(input())
D = {}
for i in range(n):
    s = input()
    if s[0] in D: D[s[0]] += 1
    else: D[s[0]] = 1

ans = []
for x in D.keys(): # for x in D: 도 가능
    if D[x] >= 5: ans.append(x)

if len(ans) == 0: print('PREDAJA')
else:
    ans.sort()
    print(''.join(ans))