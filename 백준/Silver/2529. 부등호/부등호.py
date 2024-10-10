k = int(input())
inqs = list(map(str, input().split()))

# check의 결과가 True이면 부등호에 맞는 것
def check(num1, num2, inq) :  
  if inq == '<' :
    return num1 < num2
  else :
    return num1 > num2

def dfs() :

  global min_answer, max_answer

  if len(temp) == (k+1) :
    # 최대랑 최소 업데이트
    if len(min_answer) == 0 :  # 가장 먼저 생성된 값 : 최소
      min_answer = [i for i in temp]
    else :  # 가장 마지막에 생성된 값 : 최대
      max_answer = [i for i in temp]

  for i in range(10) :
    if visited[i] == False :
      # 조건 추가해서 부등호를 만족하는지를 바로바로 체크해주는게 중요!!
      if len(temp) <= k :
        if len(temp) == 0 or check(temp[-1], i, inqs[len(temp)-1]) :
          temp.append(i)
          visited[i] = True
          dfs()
          temp.pop()
          visited[i] = False
        
temp = []
visited = [False] * 10
min_answer = []
max_answer = []
dfs()
print(''.join([str(i) for i in max_answer]))
print(''.join([str(i) for i in min_answer]))