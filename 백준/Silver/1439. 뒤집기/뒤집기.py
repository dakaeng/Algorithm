S = input()

count = [0, 0]
char = S[0]
count[int(char)] += 1

for idx, s in enumerate(S[1:]) :
  if s == char :
    continue
  else :
    count[int(s)] += 1
    char = S[idx+1]
    
print(min(count))