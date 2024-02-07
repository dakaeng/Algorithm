N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

price = price[:-1]
total = 0
dist = sum(length)
for i in range(len(length)) :
  if dist == 0 :
    break
  else :
    if price[i] == min(price[i:]) :
      total += price[i] * sum(length[i:])
      dist -= sum(length[i:])
    else :
      total += price[i] * length[i]
      dist -= length[i]
print(total)