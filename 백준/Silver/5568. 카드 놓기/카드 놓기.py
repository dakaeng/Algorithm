n = int(input())
k = int(input())

cards = []
for _ in range(n) :
  cards.append(input())  # str으로 받기 -> 나중에 연결하는 연산 편리

from itertools import permutations
perms = list(permutations(range(n), k))
nums = []

for p in perms :
  temp = ''
  for i in p :
    temp += cards[i]
  nums.append(temp)
print(len(set(nums)))