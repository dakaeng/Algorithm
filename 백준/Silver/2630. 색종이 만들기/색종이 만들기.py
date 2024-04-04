N = int(input())
paper = []
for _ in range(N) :
  paper.append(list(map(int, input().split())))

def paper_count(paper) :
  # 현재 종이가 전부 같은 색인지 판단
  # 같은 색이면 -> count에 추가
  n = len(paper)
  sum_paper = 0
  for i in range(n) :
    sum_paper += sum(paper[i])
  if sum_paper == 0 :  # 종이가 전부 하얀색
    count[0] += 1
  elif sum_paper == n**2 :  # 종이가 전부 파란색
    count[1] += 1
  # 다른 색이면 -> 나누기(4조각이 됨)
  else :  # 종이에 색이 섞여있음
    temp = split_paper(paper)  # 데이터셋 4개에 대해서 paper_count 실행
    paper_count(temp[0])
    paper_count(temp[1])
    paper_count(temp[2])
    paper_count(temp[3])
    
def split_paper(paper) :
  data1 = []
  data2 = []
  data3 = []
  data4 = []

  n = len(paper)
  for i in range(n) :
    if i < (n//2) :
      data1.append(paper[i][0:(n//2)])
      data2.append(paper[i][(n//2):])
    else :
      data3.append(paper[i][0:(n//2)])
      data4.append(paper[i][(n//2):])
  
  return data1, data2, data3, data4

count = [0, 0]
paper_count(paper)
for i in count :
  print(i)