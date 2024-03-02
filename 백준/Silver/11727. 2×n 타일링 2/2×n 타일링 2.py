n = int(input())
answer = [0] * (n+1)
answer[1] = 1
if n > 1 :
  answer[2] = 3
if n > 2 :
  for i in range(3, n+1) :
    answer[i] = (answer[i-1] + answer[i-2] * 2) % 10007
print(answer[n])