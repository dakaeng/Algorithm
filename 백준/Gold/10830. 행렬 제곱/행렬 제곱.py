N, B = map(int, input().split())
A = []
for _ in range(N) :
  A.append(list(map(int, input().split())))

# 행렬곱 계산하는 부분
def mul(A, B) :
  n = len(A)
  answer = [[0 for _ in range(n)]for _ in range(n)]

  for i in range(n) :
    for j in range(n) :
      for k in range(n) :
        answer[i][j] += A[i][k] * B[k][j]
      answer[i][j] %= 1000
  return answer

def power(A, B) :
  N = len(A)
  if B == 1 :
    for i in range(N) :
      for j in range(N) :
        A[i][j] %= 1000
    return A

  tmp = power(A, B//2)
  if B % 2 : 
    return mul(mul(tmp, tmp), A)
  else :
    return mul(tmp, tmp)

answer = power(A, B)
for i in answer :
  print(*i)