import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
Xset = set(X)
Xlist = list(Xset)
Xlist.sort()

Xdic = {}

for idx, x in enumerate(Xlist) :
    Xdic[x] = idx
Xdic = dict(sorted(Xdic.items()))
for x in X :
    print(Xdic[x], end = ' ')