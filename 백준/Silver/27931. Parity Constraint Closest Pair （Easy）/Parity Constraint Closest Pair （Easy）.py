N = int(input())
nums = list(map(int, input().split()))

nums.sort()
INF = 2 * 1e9 + 1
even_min, odd_min = INF, INF  # 거리 짝수 정답, 거리 홀수 정답
even_idx, odd_idx = None, None  # 마지막 짝수, 홀수 인덱스

# 거리가 짝수 : 둘다 짝수 or 둘다 홀수
# 거리가 홀수 : 둘 중 하나 짝수, 하나 홀수
for i in range(N) :
  if nums[i] % 2 == 0 :  # nums[i]가 짝수
    if even_idx != None :
      even_min = min(even_min, nums[i] - nums[even_idx])  # 짝수 - 짝수 = 짝수
    if odd_idx != None :
      odd_min = min(odd_min, nums[i] - nums[odd_idx])  # 짝수 - 홀수 = 홀수
    even_idx = i
  else :  # nums[i]가 홀수
    if even_idx != None :
      odd_min = min(odd_min, nums[i] - nums[even_idx])  # 홀수 - 짝수 = 홀수
    if odd_idx != None :
      even_min = min(even_min, nums[i] - nums[odd_idx])  # 홀수 - 홀수 = 짝수
    odd_idx = i

print(even_min if even_min != INF else -1, odd_min if odd_min != INF else -1)