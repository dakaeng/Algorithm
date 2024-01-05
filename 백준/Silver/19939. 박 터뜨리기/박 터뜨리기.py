N, K = map(int, input().split())
basket = [0] * K

for i in range(len(basket)) :
  basket[i] = (i+1)

if N < sum(basket) :
  print(-1)
elif N == sum(basket) :
  print(max(basket) - min(basket))
else :
  ball = N - sum(basket)
  basket = basket[::-1]
  i = 0
  while (ball != 0) :
    basket[i] +=1 
    ball -= 1
    i += 1
    if i == K :
      i = 0
  print(max(basket) - min(basket))