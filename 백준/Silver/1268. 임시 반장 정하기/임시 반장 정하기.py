N = int(input())
nums = []  # 각 학생의 과거 반 정보 저장
for _ in range(N) :
  nums.append(list(map(int, input().split())))

# 학생별, 학년별 정보 살펴보면서 같은 반이었던 학생 수 count
count = [[] for _ in range(N)]
for s in range(N-1) :
  for i in range(5) :  # 학년
    for j in range(s+1, N) :  # 학생
      if nums[s][i] == nums[j][i] :
        count[s].append(j+1)
        count[j].append(s+1)
temp = []
for i in count :
  temp.append(len(set(i)))
print(temp.index(max(temp)) + 1)