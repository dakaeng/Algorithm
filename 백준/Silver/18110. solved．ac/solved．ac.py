import sys
input = sys.stdin.readline
n = int(input())
level = []
if n == 0 :
    print(0)
else :
    for _ in range(n) :
        level.append(int(input()))
    level.sort()
    num = round(len(level) * 0.15 + 1e-5)
    print(round(sum(level[num:(len(level)-num)]) / (len(level)-2*num) + 1e-5))