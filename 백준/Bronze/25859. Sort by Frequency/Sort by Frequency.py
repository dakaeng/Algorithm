from collections import Counter

S = input()
sort_dict = sorted(Counter(S).items(), key = lambda x : (-x[1], x[0]))

for i in sort_dict :
  print(i[0] * i[1], end = '')