for _ in range(4) :
  x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
  
  # 공통부분 없음
  if x1 > p2 or y1 > q2 or p1 < x2 or q1 < y2 :
    print('d')
    continue

  elif x1 == p2 or x2 == p1 :
    # 선분
    if q1 == y2 or q2 == y1 :
      print('c')
      continue
    # 점
    else :
      print('b')
      continue
  # 점
  elif q1 == y2 or q2 == y1 :
    print('b')
    continue

  # 직사각형
  else :
    print('a')
    continue