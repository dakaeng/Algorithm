N = int(input())

words = []
for _ in range(N) :
  words.append(input())

answer = 'YES'
for i in range(N) :
  for j in range(i, N) :
    if words[i][j] != words[j][i] :
      answer = 'NO'
      break
print(answer)