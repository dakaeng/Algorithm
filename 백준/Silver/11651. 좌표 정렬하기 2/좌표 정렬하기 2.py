N = int(input())
XY = []
for n in range(N) :
    x, y = map(int, input().split())
    XY.append([x, y])
XY.sort(key = lambda i: (i[1], i[0]))
for x,y in XY :
    print(x, y)