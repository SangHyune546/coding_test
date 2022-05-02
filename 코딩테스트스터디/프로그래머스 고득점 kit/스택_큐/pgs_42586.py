def solution(progresses, speeds):
    
    answer = []
    
    while progresses:
        
        if progresses[0] < 100:
            
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
                
        else:
            cnt = 0
            
            for i in range(len(progresses)):
                
                if progresses[i] >= 100:                             
                    cnt += 1
                else:
                    break
                    
            if cnt == 1:
                progresses.pop(0)
                speeds.pop(0)
                answer.append(cnt)      
                
            else:   
                
                for i in range(cnt):
                    progresses.pop(0)
                    speeds.pop(0)
                answer.append(cnt)
            
    return answer