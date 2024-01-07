N, K, P = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
for i in range(N) :
  if ( K - sum(nums[(i*K):(i*K+K)]) ) < P :
    answer += 1
print(answer)