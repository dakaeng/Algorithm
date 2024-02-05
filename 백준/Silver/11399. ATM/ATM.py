N = int(input())
P = list(map(int, input().split()))
P.sort()
sums = []
temp = 0
for t in P :
  temp += t
  sums.append(temp)
print(sum(sums))