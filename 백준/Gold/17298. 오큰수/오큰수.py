N = int(input())
A = list(map(int, input().split()))

# 스택 사용한 풀이 해보기
answer = [-1] * N
stack = []

for i in range(N) :
  while (stack and A[stack[-1]] < A[i]) :
    answer[stack[-1]] = A[i]
    stack.pop()
  stack.append(i)
print(*answer)