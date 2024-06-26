d1, d2, x = map(int, input().split())

if d1 < d2 :
  d1, d2 = d2, d1  # d1 : 밀도 높은 금속

# 계산하기 쉽게 전체 질량은 100이라고 가정
weight1 = x
weight2 = 100 - x

# 부피
vol1 = weight1 / d1
vol2 = weight2 / d2

# 기념주화의 밀도
print(100 / (vol1 + vol2))