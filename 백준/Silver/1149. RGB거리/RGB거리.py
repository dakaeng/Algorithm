N = int(input())
prices = [[0, 0, 0]]
for _ in range(N) :
  prices.append(list(map(int, input().split())))
  
total_price = [[0, 0, 0] for _ in range(N+1)]
total_price[1] = prices[1]

for i in range(2, N+1) :
  total_price[i][0] = prices[i][0] + min(total_price[i-1][1], total_price[i-1][2])
  total_price[i][1] = prices[i][1] + min(total_price[i-1][0], total_price[i-1][2])
  total_price[i][2] = prices[i][2] + min(total_price[i-1][0], total_price[i-1][1])
print(min(total_price[N]))