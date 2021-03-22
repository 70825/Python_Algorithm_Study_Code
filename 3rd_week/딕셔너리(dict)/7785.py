company = dict() # d = {}
n = int(input())
for i in range(n):
    x, y = input().split()
    company[x] = y

key = list(company.keys())
ans = []
for i in range(len(key)):
    if company[key[i]] == 'enter':
        ans.append(key[i])

# ans = sorted(ans)[::-1] 또는 ans = sorted(ans, reverse= True)
ans.sort(reverse = True)
for i in range(len(ans)):
    print(ans[i])