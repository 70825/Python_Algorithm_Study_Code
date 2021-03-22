while True:
    s = input()
    if s == '*': break
    D = {}
    for i in range(26):
        D[chr(97+i)] = 0
    
    for i in range(len(s)):
        # ord('a') <= ord(s[i]) <= ord('z')도 가능
        if 97 <= ord(s[i]) <= 122:
            D[s[i]] += 1
    
    #처음엔 알파벳이 모두 있다고 가정하고 나중에 False로 변경
    flag = True
    key = list(D.keys())
    for i in range(len(key)):
        if D[key[i]] == 0:
            flag = False
    if flag == True: print('Y')
    else: print('N')