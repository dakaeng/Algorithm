H, Y = map(int, input().split())

d = [0] * 11

d[0] = H
d[1] = int(d[0] * 1.05)
d[2] = int(d[1] * 1.05)
d[3] = int(d[0] * 1.2)
d[4] = max(int(d[3] * 1.05), int(int(d[2] * 1.05) * 1.05))

for i in range(4, Y+1) :
  d[i] = max(int(d[i-5] * 1.35), int(d[i-3] * 1.2), int(d[i-1] * 1.05))

print(d[Y])