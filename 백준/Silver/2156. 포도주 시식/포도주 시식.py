n = int(input())
wine = []
for _ in range(n) :
  wine.append(int(input()))

d = [0] * n
d[0] = wine[0]
if n > 1 :
  d[1] = d[0] + wine[1]
if n > 2 :
  d[2] = max(d[0] + wine[2], wine[1] + wine[2], d[1])  # 세번째 와인을 마시지 않는 경우도 고려
if n > 3 :
  for i in range(3, n) :
    d[i] = max(d[i-2] + wine[i], wine[i-1] + d[i-3] + wine[i], d[i-1])  # (i+1)번째 와인을 마시지 않는 경우도 고려
print(max(d))