from itertools import combinations

T = int(input())
for _ in range(T) :
  n = int(input())
  answer = 1
  clothes = {}
  for _ in range(n) :
    cloth_name, cloth_type = input().split()
    if cloth_type in clothes.keys() :
      clothes[cloth_type].append(cloth_name)
    else :
      clothes[cloth_type] = [cloth_name]
  for i in clothes.keys() :
    temp = len( list(combinations(clothes[i], 0)) ) + len( list(combinations(clothes[i], 1)) )
    answer *= temp
  print(answer-1)