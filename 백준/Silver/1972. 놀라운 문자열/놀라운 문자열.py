def surprise(string) :
  for d in range(len(string)-2) :  # (N-2)쌍은 한 개이므로 굳이 고려할 필요 없음
    dic = {}
    for i in range(len(string)-d-1) :
      temp = string[i] + string[i+d+1]
      if temp in dic :
        dic[temp] += 1
      else :
        dic[temp] = 1
    for i in dic :
      if dic[i] >= 2 :
        return False
  return True

while True :
  string = input()
  if string == '*' :
    break
  
  if len(string) <= 2 :
    answer = True
  else :
    answer = surprise(string)
  
  if answer :
    print('{} is surprising.'.format(string))
  else :
    print('{} is NOT surprising.'.format(string))