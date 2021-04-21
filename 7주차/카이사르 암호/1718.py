s = list(input())
key = input()

for i in range(len(s)):
    if ord('a') <= ord(s[i]) <= ord('z'):
        x = ord(s[i])-97
        y = ord(key[i%len(key)])-96
        s[i] = chr((x-y+26)%26+97)

print(''.join(s))