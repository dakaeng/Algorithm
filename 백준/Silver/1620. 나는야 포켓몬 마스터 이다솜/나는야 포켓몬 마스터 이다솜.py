import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = {}
for n in range(N) :
    poketmon[input().strip()] = n+1
names = list(poketmon.keys())
for _ in range(M) :
    quest = input().strip()
    if quest.isalpha() :
        print(poketmon[quest])
    else :
        print(names[int(quest)-1])