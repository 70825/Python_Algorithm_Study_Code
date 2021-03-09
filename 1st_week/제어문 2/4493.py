t = int(input())
while t:
    t -= 1
    n = int(input())
    x,y = 0,0
    for j in range(n):
        a,b = input().split()
        if a == 'R':
            if b == 'P': y += 1
            elif b == 'S': x += 1
        if a == 'S':
            if b == 'R': y += 1
            if b == 'P': x += 1
        if a == 'P':
            if b == 'S': y += 1
            if b == 'R': x += 1
    if x == y:print('TIE')
    elif x > y: print('Player 1')
    else:print('Player 2')