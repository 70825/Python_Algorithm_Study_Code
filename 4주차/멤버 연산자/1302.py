n = int(input())
d = {}
for i in range(n):
    s = input()
    if s not in d: d[s] = 1
    else: d[s] += 1
x = max(d.values())
y = sorted(list(d.keys()))

for book in y:
    if d[book] == x:
        print(book)
        break