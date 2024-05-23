import sys
input = sys.stdin.readline

trees = {}
tree_name = []
count = 0

while True :
  tree = input().strip()
  if not tree :
    break

  count += 1
  if tree in trees :
    trees[tree] += 1
  else :
    trees[tree] = 1
    tree_name.append(tree)
    
tree_name.sort()
for tree in tree_name :
  print(tree, '{:.4f}'.format((trees[tree]/count) * 100))