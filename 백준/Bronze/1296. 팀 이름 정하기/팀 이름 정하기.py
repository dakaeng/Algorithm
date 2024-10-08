name = input()
N = int(input())
team_name = []
for _ in range(N) :
  team_name.append([input(), 0])

def LOVE_count(name) :
  for n in name :
    if n == 'L' :
      temp[0] += 1
    elif n == 'O' :
      temp[1] += 1
    elif n == 'V' :
      temp[2] += 1
    elif n == 'E' :
      temp[3] += 1
    
team_name.sort()

for idx, t in enumerate(team_name) :
  temp = [0 for _ in range(4)]
  LOVE_count(name)
  LOVE_count(t[0])

  p = 1
  for i in range(3) :
    for j in range(i+1, 4) :
      p *= (temp[i] + temp[j])
  p = p % 100
  team_name[idx][1] = p

team_name.sort(key = lambda x : (-x[1], x[0]))
print(team_name[0][0])