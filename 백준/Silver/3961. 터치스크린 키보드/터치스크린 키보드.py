screen = [['q','w','e','r','t','y','u','i','o','p'],
          ['a','s','d','f','g','h','j','k','l'],
          ['z','x','c','v','b','n','m']]

def distance(a, b) :  # 문자 a와 b 사이의 거리 계산하는 함수
  a_xy, b_xy = [], []
  for i in range(3) :
    if a in screen[i] :
      a_xy.extend([i, screen[i].index(a)])
    if b in screen[i] :
      b_xy.extend([i, screen[i].index(b)])
  dx = a_xy[0] - b_xy[0]
  dy = a_xy[1] - b_xy[1]
  dist = (dx if dx > 0 else -dx) + (dy if dy > 0 else -dy)
  return dist

t = int(input())
for _ in range(t) :
  word, l = input().split()
  answer = []
  for _ in range(int(l)) :
    cand = input()
    dist = 0
    for i in range(len(cand)) :
      if word[i] != cand[i] :  # 다를 때만 거리 계산
        dist += distance(word[i], cand[i])
    answer.append((cand, dist))
  answer.sort(key = lambda x : (x[1], x[0]))
  for i in answer :
    print(*i)