N = int(input())
correct = list(input().split())  # 올바른 정답
answer = list(input().split())  # 현우가 작성한 답

dic = {}  # 해전 순서 저장
for i in range(N) :
  dic[correct[i]] = i

score = 0
for i in range(N-1) :
  for j in range(i+1, N) :
    if dic[answer[i]] < dic[answer[j]] :  # 어차피 상대적인 순서만 알면 됨
      score += 1
print('{}/{}'.format(score, int(N*(N-1)/2)))