N, K = map(int, input().split())
A = list(map(int, input().split()))

if set(A) == {1} or set(A) == {2} :  # 다 1학년이거나 2학년인 경우
  answer = N

else :
  answer = 0

  while (len(A) > 0) :
    answer += 1

    left = A[0:K]
    right = A[K:]
    if len(set(left)) == 1 :
      left.pop()
      A = left + right
    else :
      a = left.pop()
      b = []
      for _ in range(K-1) :
        if a == left[-1]  :
          b.append(left.pop())
        else :
          left.pop()
          b.extend(left[::-1])
      A = b[::-1] + right
    
print(answer)