N = int(input())
list1 = list(map(int, input().split()))
M = int(input())
list2 = list(map(int, input().split()))

dict1 = {}
answer = []
for i in list1 :
  if i in dict1 :
    dict1[i] += 1
  else :
    dict1[i] = 1

for i in list2 :
  if i in dict1 :
    answer.append(dict1[i])
  else :
    answer.append(0)
print(*answer)