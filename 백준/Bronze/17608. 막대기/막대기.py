import sys
input = sys.stdin.readline

N = int(input())
sticks = []
for _ in range(N) :
  sticks.append(int(input()))
sticks = sticks[::-1]

count = 1
h0 = sticks[0]  # 기준이 되는 막대기
for h in sticks[1:] :
  if h > h0 :
    count += 1
    h0 = h
print(count)