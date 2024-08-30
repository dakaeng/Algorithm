import sys
input = sys.stdin.readline

N = int(input())
book = []
for _ in range(N) :
  book.append(int(input()))

# book[0] : 가장 위, book[N] : 가장 아래
idx = book.index(N)
answer = N - idx - 1
temp = N
for i in range(idx-1, -1, -1) :
  if book[i] == (temp - 1) :
    temp = book[i]
  else :
    answer += 1
print(answer)