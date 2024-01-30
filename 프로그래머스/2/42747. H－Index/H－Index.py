def solution(citations):
    answer = 0
    # [3, 0, 6, 1, 5] -> 3
    count = [0] * (max(citations) + 1)
    for i in citations :
        count[i] += 1
    for i in range(len(count)-1, -1, -1) :
        if sum(count[i:]) >= i :
            answer = i
            break
    return answer