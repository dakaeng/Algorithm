N = int(input())
step = [0]
for _ in range(N) :
  step.append(int(input()))

scores = [0 for _ in range(N+1)]
if N >= 1 :
  scores[1] = step[1]
if N >= 2 :
  scores[2] = step[1] + step[2]
if N >= 3 :
  scores[3] = max(step[1], step[2]) + step[3]
if N > 3 :
  for i in range(4, N+1) :
    scores[i] = step[i] + max(step[i-1] + scores[i-3], scores[i-2])
print(scores[N])