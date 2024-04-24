N = int(input())

answer = 0
for _ in range(N) :
  word = input()

  # stack에 단어를 한 글자씩 입력한 후, 다음 글자와 stack의 마지막 글자 비교
  stack = [word[0]]
  for i in range(1, len(word)) :
    if stack and word[i] == stack[-1] :  # 같다면 -> 짝이 지어진 것이므로 stack에서 제거
      stack.pop()
    else :
      stack.append(word[i])

  # stack에 원소가 남아있지 않으면, 모든 글자가 짝지어진 것 -> 좋은 글자
  if not stack :
    answer += 1

print(answer)