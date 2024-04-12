abc = list(map(int, input().split()))
abc.sort()
a, b, c = abc[0], abc[1], abc[2]

if c < (a + b) :
  answer = (a + b + c)
else :
  answer = 2 * (a + b) - 1
print(answer)