import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

price = price[:-1]
total = 0
min_prices = min(price)

if price[0] == min_prices :
  sum_length = sum(length)
  total += price[0] * sum_length
  
else :
  total += price[0] * length[0]
  for i in range(1, N-1) :
    if price[i-1] < price[i] :
      price[i] = price[i-1]
    total += price[i] * length[i]
print(total)