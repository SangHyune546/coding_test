from collections import deque

def solution(priorities, location):
    
    answer = 0
    flag = True
    
    priorities = deque(priorities)
    
    for i in range(len(priorities)):
        priorities[i] = ((priorities[i],i))
    
    while True:
        
        j = priorities.popleft()

        if len(priorities) > 0 and max(priorities)[0] > j[0]:
            priorities.append(j)

        else:
            answer += 1
            if j[1] == location:
                break
    
    return answer
