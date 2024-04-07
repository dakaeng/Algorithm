import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = {}  # 키 : 길이가 M 이상인 단어, 값 : 단어의 등장 횟수
for _ in range(N) :
  word = input().rstrip()
  if len(word) >= M  :
    if word not in words :
      words[word] = 1
    else :
      words[word] += 1
    
words = dict(sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0])))
for w in words :
  print(w)