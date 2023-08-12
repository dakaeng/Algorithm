S = input() + ' '
stack = []
answer = ''
word = True
for s in S :
    if s == '<' :
        word = False
        for _ in range(len(stack)) :
            answer += stack.pop()
    stack.append(s)
    if s == '>' :
        word = True
        for _ in range(len(stack)) :
            answer += stack.pop(0)
    if word and s == ' ' :
        stack.pop()
        for _ in range(len(stack)) :
            answer += stack.pop()
        answer += ' '
print(answer)