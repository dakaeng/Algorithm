from collections import deque
N = int(input())
cards = deque([i for i in range(N, 0, -1)])

while True :
    if len(cards) == 1 :
        break
    cards.pop()
    a = cards.pop()
    cards.appendleft(a)

print(*cards)