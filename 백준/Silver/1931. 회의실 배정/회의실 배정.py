N = int(input())
XY = []
for _ in range(N) :
    x, y = map(int, input().split())
    XY.append([x, y])
XY.sort(key = lambda i: [i[1], i[0]])

end = XY[0][1]
count = 1
for s, e in XY[1:] :
  if s >= end :
    end = e
    count += 1
print(count)