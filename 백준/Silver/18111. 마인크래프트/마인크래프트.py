from collections import Counter
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
heights = []
for _ in range(N) :
    heights += list(map(int, input().split()))

counter = Counter(heights).items()
answer = 0
time = 999999999
for i in range(min((B + sum(heights)) // (N * M), max(heights)), -1, -1) :
    count = 0
    for k, ct in counter :
        if k > i :  # 현재 층보다 블록 높이가 높으면
            count += (k-i) * ct * 2  # (블록 높이 - 현재 층) 만큼 블록 제거
        else :
            count += (i-k) * ct
    if count < time :  # 답이 여러 개인 경우, 땅의 높이가 가장 높은 것이 출력되도록
        time = count
        answer = i
    else :
        break
print(time, answer)