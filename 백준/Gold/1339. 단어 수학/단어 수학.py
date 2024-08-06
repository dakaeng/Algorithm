N = int(input())
words = []
for _ in range(N) :
  words.append(input())

word_dic = {}

for word in words :
  n = len(word)
  for idx, alpha in enumerate(word) :
    if alpha in word_dic :
      word_dic[alpha] += 10**(n-idx-1)
    else :
      word_dic[alpha] = 10**(n-idx-1)
    
word_num = sorted(word_dic.values(), reverse = True)
answer = 0
num = 9
for i in range(len(word_num)) :
  answer += word_num[i] * num
  num -= 1
print(answer)