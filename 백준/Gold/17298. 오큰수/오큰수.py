N = int(input())
A = list(map(int, input().split()))

NGE = [-1] * N  # NGE[i] : A_i의 오큰수 저장
stack = []

for i in range(N) :
  while (stack and A[stack[-1]] < A[i]) :  # A[i]가 A[stack[-1]]의 오큰수가 되는 경우
    NGE[stack[-1]] = A[i]  # 저장
    stack.pop()  # A[stack[-1]]의 오큰수를 구했으므로 stack에서 해당 인덱스 값 제거
  stack.append(i)
print(*NGE)