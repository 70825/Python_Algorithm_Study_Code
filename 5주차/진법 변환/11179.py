n = int(input())
x = bin(n)[2:]
print(int(x[::-1],2))