def choose_num(start) :
  if len(selected_idx) == 6 :  # 6개 숫자를 모두 뽑았으면 결과 출력
    for idx in selected_idx :
      print(S[idx], end = ' ')
    print()
    
  for i in range(start, len(S)) :  # 순서 상관없이 겹치지 않게 뽑아야 하므로 start 지정
    selected_idx.append(i)
    choose_num(i + 1)
    selected_idx.pop()
    
while True :
  k, *S = map(int, input().split())
  if k == 0 :
    break

  selected_idx = []  # S의 인덱스를 뽑아서 저장
  choose_num(0)
  print()