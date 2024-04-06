n = int(input())
amount = []

for _ in range(n) :
  amount.append(int(input()))

d = [0] * n
if n >= 1 :
    d[0] = amount[0]   
if n >= 2 :
    d[1] = amount[0] + amount[1]
if n >= 3 :
    d[2] = max(amount[0] + amount[2], amount[1] + amount[2], d[1])  # 2번째 와인을 마시지 않는 경우도 고려
if n >= 4 :
    for i in range(3, n) :
        d[i] = max(d[i-2] + amount[i], d[i-3] + amount[i-1] + amount[i], d[i-1])
print(max(d))