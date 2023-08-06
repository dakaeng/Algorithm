from collections import deque
N = int(input())
balloons = list(map(int, input().split()))
deque = deque([(num, idx+1) for idx, num in enumerate(balloons)])
answer = []
idx = 0

while True :
    (num, idx) = deque.popleft()
    answer.append(idx)
    if not deque :
        break
    if num > 0 :
        for _ in range(num-1) :
            deque.append(deque.popleft())
    else :
        for _ in range(-num) :
            deque.appendleft(deque.pop())
print(*answer)