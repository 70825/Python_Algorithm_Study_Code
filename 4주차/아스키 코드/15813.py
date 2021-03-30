score = {chr(65+i): i+1 for i in range(26)}

n = int(input())
s = input()

ans = 0
for i in range(n):
    ans += score[s[i]]
print(ans)