from collections import deque
n = int(input())
for _ in range(n) :
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    idx = deque([i for i in range(N)])
    answer = 0
    while (M in idx) :
        if importance[0] < max(importance) :
            importance.append(importance.popleft())
            idx.append(idx.popleft())
        elif importance[0] == max(importance) :
            importance.popleft()
            idx.popleft()
            answer += 1
    print(answer)