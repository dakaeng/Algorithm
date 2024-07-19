from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

# S의 모든 부분 수열의 합 구해놓기
sums = []
for i in range(1, N+1) :  # 부분 수열의 원소 개수
  comb = combinations(S, i)
  for c in comb :
    sums.append(sum(c))
sums = list(set(sums))
sums.sort()

# 1부터 sum(S)까지의 숫자 중 부분 수열의 합으로 나올 수 없는 숫자 찾기
n = 0
for i in sums :
  if (n+1) == i :
    n += 1
    continue
  else :
    break
print(n+1)