from collections import defaultdict

def solution(clothes):
    

    answer = 1
    
    c_dict = defaultdict(list)
    
    for cloth in clothes:
        c_dict[cloth[1]].append(cloth[0])
        
    
    for key in c_dict.keys():
        
        answer *= len(c_dict[key]) + 1
            
            
    return answer - 1