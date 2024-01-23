def solution(array, commands):
    answer = []
    for c in commands :
        i = c[0]; j = c[1]; k = c[2]
        result = sorted(array[(i-1):j])
        answer.append(result[k-1])
    return answer