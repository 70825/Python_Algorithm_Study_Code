while True:
    s = input()
    if s == 'EOI': break
    s = s.lower()

    flag = False
    for i in range(len(s)):
        if s[i:i+4] == 'nemo':
            flag = True
            break #break문은 없어도 가능
    if flag == True: print('Found')
    else: print('Missing')