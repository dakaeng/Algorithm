def solution(numbers):
    if list(set(numbers)) == [0] :  # numbers의 모든 원소가 0인 경우
        return '0'
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : (x*4)[:4], reverse = True)
    for n in numbers :
        answer += n
    return answer