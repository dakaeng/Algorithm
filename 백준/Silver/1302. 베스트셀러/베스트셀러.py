N = int(input())
sale = {}

for _ in range(N) :
  title = input()
  if title in sale :
    sale[title] += 1
  else :
    sale[title] = 1
    
titles = list(dict(sorted(sale.items(), key = lambda x : (-x[1], x[0]))).keys())
print(titles[0])