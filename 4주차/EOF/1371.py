d = {chr(97+i): 0 for i in range(26)}
while 1:
    try:
        s = input()
        for i in range(len(s)):
            if 97 <= ord(s[i]) <= 122:
                d[s[i]] += 1
    except EOFError:
        break

ans = []
max_val = max(d.values())
for key in d.keys():
    if d[key] == max_val:
        ans.append(key)
print(''.join(ans))