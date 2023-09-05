T = int(input())
for _ in range(T) :
    k = int(input())
    n = int(input())
    apart = [[0 for _ in range(n)] for _ in range(k+1)]
    apart[0][0:n] = [i for i in range(1, n+1)]
    floor = 1
    temp = 0
    while True :
        if floor == (k+1) :
            break
        for i in range(n) :
            temp += apart[floor-1][i]
            apart[floor][i] = temp
        temp = 0
        floor += 1
    print(apart[k][n-1])