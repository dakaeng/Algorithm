N = int(input())
score = []
for _ in range(N) :
  score.append(int(input()))

score_r = score[::-1]  # 레벨 높은 순으로 정렬

answer = 0
s = score_r[0]
for i in range(1, len(score_r)) :
  # 더 낮은 레벨의 점수가 높은 경우, 조정 필요
  if score_r[i] >= s :
    answer += (score_r[i] - s + 1)
    score_r[i] = (s - 1)
  s = score_r[i]
print(answer)