from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    
    p_dict = defaultdict(list)
    
    for i in participant:
        
        if i not in p_dict:
            p_dict[i] = 1
            
        else:
            
            p_dict[i] = p_dict[i] + 1
            
    
    for i in completion:
        
        if i in p_dict:
            p_dict[i] = p_dict[i] - 1
            
            
            
    for key,value in p_dict.items():
        
        if value > 0:
            answer = key
    

    
    return answer