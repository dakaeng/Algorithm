T = int(input())
for _ in range(T) :
    N = int(input())
    hist = [[0, 0] for _ in range(N+1)]
    n = 0
    while (n <= N) :
        if n == 0 :
            hist[0][0] += 1
        elif n == 1 :
            hist[1][1] += 1
        else :
            hist[n][0] = hist[n-1][0] + hist[n-2][0]
            hist[n][1] = hist[n-1][1] + hist[n-2][1]
        n += 1
    print(hist[N][0], hist[N][1])