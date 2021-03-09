input = __import__('sys').stdin.readline
n = int(input())
plug = 0
for i in range(n):
    plug += int(input())
print(plug - (n - 1))