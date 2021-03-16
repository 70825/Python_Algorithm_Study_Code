t = int(input())
for i in range(t):
    arr = tuple(input())
    score = 0 #총 점수
    x = 0 #더할 점수
    for j in range(len(arr)):
        # if/else로 O가 나오면 x에 1점을 추가하고, X면 x = 0으로 만들어주고 더함
        if arr[j] == 'O': x += 1
        else: x = 0
        score += x
    print(score)