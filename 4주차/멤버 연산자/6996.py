t = int(input())
for i in range(t):
    d = {}
    for j in range(26): #chr(97) = a, chr(122) = z
        d[chr(97+j)] = 0
    A, B = input().split()

    for j in range(len(A)):
        d[A[j]] += 1
    for j in range(len(B)):
        d[B[j]] -= 1

    flag = True
    for x in d.keys():
        if d[x] != 0:
            flag = False

    if flag == True:
        print('{} & {} are anagrams.'.format(A,B))
    else:
        print('{} & {} are NOT anagrams.'.format(A, B))