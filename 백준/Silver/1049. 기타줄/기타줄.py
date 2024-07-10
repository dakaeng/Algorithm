N, M = map(int, input().split())
cost = []
for _ in range(M) :
  six, one = map(int, input().split())
  cost.append([six, one])

answer = []
# 패키지 몇 개 구매할 수 있는지 확인
pack = N // 6
each = N % 6
cost_pack = sorted(cost, key = lambda x : x[0])  # 패키지 가격 오름차순으로 정렬
cost_each = sorted(cost, key = lambda x : x[1])
answer.append(cost_pack[0][0] * pack + cost_each[0][1] * each)
answer.append(cost_pack[0][0] * (pack + 1))  # 최소 N개의 줄을 구매하는 것
answer.append(cost_each[0][1] * N)
print(min(answer))