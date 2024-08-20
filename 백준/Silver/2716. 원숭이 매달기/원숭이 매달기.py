N = int(input())
for _ in range(N) :
  string = input()

  max_depth = 0
  depth = 0
  for i in string :
    if i == '[' :
      depth += 1
    else :
      max_depth = max(max_depth, depth)
      depth -= 1
  print(2 ** max_depth)