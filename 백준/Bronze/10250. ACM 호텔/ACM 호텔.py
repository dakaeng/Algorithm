T = int(input())
for _ in range(T) :
    H, W, N = map(int, input().split())
    answer = ''
    Y = str(N % H)
    X = str((N // H) + 1)
    if Y == '0' :
        Y = str(H)
        X = str(N // H)
    answer += Y
    if len(X) == 1 :
        answer += '0'
    answer += X
    print(answer)