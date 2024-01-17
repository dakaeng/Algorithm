N, X = map(int, input().split())
visit = list(map(int, input().split()))

sums = []
temp = 0
for i in visit :
  temp += i
  sums.append(temp)

count_visit = [sums[X-1]]
for i in range(len(sums)-X) :
  count_visit.append(sums[i+X] - sums[i])

max_visit = max(count_visit)
if max_visit == 0 :
  print('SAD')
else :
  print(max_visit)
  print(count_visit.count(max_visit))