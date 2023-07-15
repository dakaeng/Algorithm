import sys
input = sys.stdin.readline

N = int(input())
XY = []
for n in range(N) :
    x, y = map(int, input().split())
    XY.append([x, y])
XY.sort()
for x, y in XY:
    print(x, y)