N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의 가장 큰 숫자와 B의 가장 작은 숫자가 곱해지도록!
A.sort(reverse = True)
B.sort()

answer = 0
for i in range(N) :
  answer += (A[i] * B[i])
print(answer)