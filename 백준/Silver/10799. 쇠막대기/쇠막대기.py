inputs = list(input())
stack = []
count = 0
for i in range(len(inputs)) :
  if inputs[i] == '(' :
    stack.append('(')
  else :  # 닫힌 괄호인 경우
    stack.pop()
    if inputs[i-1] == '(' :  # 직전 괄호가 열린 괄호 -> 레이저
      count += len(stack)
    else :
      count += 1
print(count)