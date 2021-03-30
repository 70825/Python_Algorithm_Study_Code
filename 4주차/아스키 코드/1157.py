s = input().upper()

apb = {chr(65+i): 0 for i in range(26)}
for i in range(len(s)):
    apb[s[i]] += 1

max_val = max(apb.values())
ans = []
for key in apb.keys():
    if apb[key] == max_val:
        ans.append(key)

if len(ans) == 1: print(ans[0])
else: print('?')