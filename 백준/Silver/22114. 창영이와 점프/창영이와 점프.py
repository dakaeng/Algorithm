N, K = map(int, input().split())
L = list(map(int, input().split()))

count = []  # 점프하지 않고 갈 수 있는 거리들 저장
temp = 1
for i in L :
  if i <= K :
    temp += 1
  else :
    count.append(temp)
    temp = 1
count.append(temp)

answer = count[0]
for i in range(len(count)-1) :
  answer = max(answer, count[i] + count[i+1])
print(answer)