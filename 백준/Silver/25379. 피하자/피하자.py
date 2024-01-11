N = int(input())
A = list(map(int, input().split()))

count_left = 0
count_right = 0
count = 0
for a in A :
  if a % 2 == 1 :
    count += 1
  else :
    count_right += count

count = 0
for a in A[::-1] :
  if a % 2 == 1 :
    count += 1
  else :
    count_left += count
print(min(count_left, count_right))