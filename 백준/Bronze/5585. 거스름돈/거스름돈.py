n = int(input())

coins = [500, 100, 50, 10, 5, 1]
money = 1000 - n
count = 0

for i in coins :
  count += (money // i)
  money = money % i
print(count)