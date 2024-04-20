T = int(input())
for _ in range(T) :
  N = int(input())
  note1 = list(map(int, input().split()))
  M = int(input())
  note2 = list(map(int, input().split()))

  dic = {}
  for n in set(note1) :
    dic[str(n)] = 1

  for n in note2 :
    if str(n) in dic :
      print(1)
    else :
      print(0)