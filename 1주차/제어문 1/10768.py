x = int(input())
y = int(input())
if x == 1:
    print('Before')
elif x == 2:
    if y < 18:
        print('Before')
    elif y == 18:
        print('Special')
    else:
        print('After')
else:
    print('After')