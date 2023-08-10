import sys
input = sys.stdin.readline

n = int(input())
names = set()
for _ in range(n) :
    name, el = input().split()
    if el == 'enter' :
        names.add(name)
    else :
        names.remove(name)

for i in sorted(names, reverse = True) :
    print(i)