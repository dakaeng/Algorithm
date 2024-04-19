import sys
input = sys.stdin.readline

N = int(input())
names = {}

for _ in range(N) :
  name = input()
  if name in names :
    names[name] += 1
  else :
    names[name] = 1

for _ in range(N-1) :
  name = input()
  names[name] -= 1
    
for i in names :
  if names[i] != 0 :
    print(i)
    break