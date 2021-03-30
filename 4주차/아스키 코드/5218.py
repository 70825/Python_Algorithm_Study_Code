t = int(input())
for i in range(t):
    a, b = input().split()

    ans = []
    for j in range(len(a)):
        x = ord(a[j]) - 64
        y = ord(b[j]) - 64
        if y >= x: z = y - x
        else: z = y + 26 - x
        ans.append(z)
    print('Distances: {}'.format(' '.join(map(str, ans))))