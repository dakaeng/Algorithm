N = int(input())
weight = []
for _ in range(N) :
  weight.append(int(input()))
weight.sort()

answer = []
for w in weight :
  answer.append(w * N)
  N -= 1
print(max(answer))