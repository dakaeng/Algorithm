n = int(input())
steps = []
for _ in range(n) :
  steps.append(int(input()))

d = [0 for _ in range(n)]
d[0] = steps[0]
if n > 1 :
  d[1] = d[0] + steps[1]
if n > 2 :
  d[2] = max(d[0] + steps[2], steps[1] + steps[2])
if n > 3 :
  for i in range(3, n) : 
    d[i] = steps[i] + max(steps[i-1] + d[i-3], d[i-2])
print(d[-1])