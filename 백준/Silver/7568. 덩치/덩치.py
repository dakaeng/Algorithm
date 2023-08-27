N = int(input())
XY = []
for _ in range(N) :
    x, y = map(int, input().split())
    XY.append([x, y])
answer = [N for i in range(N)]
for i in range(N) :
    for j in range(N) :
        if i < j :
            if (XY[i][0] > XY[j][0]) and (XY[i][1] > XY[j][1]) :
                answer[i] -= 1
            elif (XY[i][0] < XY[j][0]) and (XY[i][1] < XY[j][1]) :
                answer[j] -= 1
            else :
                answer[i] -= 1
                answer[j] -= 1
print(*answer)