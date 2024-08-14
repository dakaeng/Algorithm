n, k = map(int, input().split())
A = list(map(int, input().split()))

# 활성화시킨 후에 경험치 쌓이기 시작 -> 경험치 작은 퀘스트부터 시작하는게 유리
A.sort()
answer = 0
a = 0
for i in range(n) :
  answer += A[i] * a
  if a < k :
    a += 1
print(answer)