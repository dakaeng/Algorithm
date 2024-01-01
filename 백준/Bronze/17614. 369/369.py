import sys
input = sys.stdin.readline

N = int(input())

check = '369'
count = 0
for n in range(1, N+1) :
  n = str(n)
  for c in check :
    count += n.count(c)
print(count)