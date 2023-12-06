x = int(input())
count = [0 for i in range(x+1)]

for i in range(2, x+1) :
  count[i] = count[i-1] + 1
  if i % 3 == 0 :
    count[i] = min(count[i//3] + 1, count[i])
  if i % 2 == 0 :
    count[i] = min(count[i//2] + 1, count[i])
print(count[x])