def solution(participant, completion):
    answer = ''
    part_dic = {}
    for i in participant :
        if i in part_dic :
            part_dic[i] += 1
        else :
            part_dic[i] = 1
    for i in completion :
        part_dic[i] -= 1
        
    for i in part_dic :
        if part_dic[i] != 0 :
            answer = i
            break
            
    return answer