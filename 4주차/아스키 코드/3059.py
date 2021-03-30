val = {chr(65+i): 65+i for i in range(26)}

t = int(input())
for i in range(t):
    d = {chr(65+i): 0 for i in range(26)}
    s = input()
    for j in range(len(s)):
        d[s[j]] += 1
    ans = 0
    for key in d.keys():
        if d[key] == 0:
            ans += val[key]
    print(ans)