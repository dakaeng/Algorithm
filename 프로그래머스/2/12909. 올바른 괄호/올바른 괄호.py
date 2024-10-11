def solution(s):
    answer = True
    stack = []
    for i in range(len(s)) :
        if stack and stack[-1] == '(' and s[i] == ')' :
            stack.pop()
        else :
            stack.append(s[i])
        
    if stack :
        answer = False

    return answer