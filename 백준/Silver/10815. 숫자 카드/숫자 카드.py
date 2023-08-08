N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
answer = [0 for _ in range(M)]

sets = set(nums) - set(cards)
for idx, n in enumerate(nums) :
    if n not in sets :
        answer[idx] = 1
print(*answer)