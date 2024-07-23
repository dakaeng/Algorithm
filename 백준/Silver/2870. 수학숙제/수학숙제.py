N = int(input())
answer = []

for _ in range(N) :
  string = input()
  temp = ''
  for i in string :
    if i.isdigit() :
      temp += i
    else :
      if len(temp) > 0 :
        answer.append(int(temp))
        temp = ''
  if len(temp) > 0 :
    answer.append(int(temp))

answer.sort()
for i in answer :
  print(i)