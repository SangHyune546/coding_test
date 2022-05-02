from collections import defaultdict

def solution(genres, plays):
    
    answer = []
    
    dic = defaultdict(list)
    s_dic = defaultdict(list)
    temp = list()
    
    for i in range(len(genres)):
        if genres[i] not in dic.keys():
            dic[genres[i]] = [[[i,plays[i]]],plays[i]]
        else:
            dic[genres[i]][0].append([i,plays[i]])
            dic[genres[i]][1] += plays[i]
            

    s_dic = dict(sorted(dic.items(), key = lambda x: (-x[1][1])))
                 
    for key,value in s_dic.items():
        temp.append(value[0])
        
    for i in temp:
        i.sort(key = lambda x : -x[1])
        
    for i in temp:
        if len(i) == 1:
            answer.append(i[0][0])
        else:
            
            for j in range(2):
                answer.append(i[j][0])

    return answer


def solution2(genres, plays):
    
    answer = []
    
    dic = defaultdict(list)
    s_dic = defaultdict(list)
    
    temp = list()
    
    for i in range(len(genres)):
        if genres[i] not in dic.keys():
            dic[genres[i]] = [[[i,plays[i]]],plays[i]]
        else:
            dic[genres[i]][0].append([i,plays[i]])
            dic[genres[i]][1] += plays[i]
            

    s_dic = dict(sorted(dic.items(), key = lambda x: (-x[1][1])))
                 
    for key,value in s_dic.items():
        temp.append(value[0])
        
    for i in temp:
        i.sort(key = lambda x : -x[1])
        
    for i in temp:
        if len(i) == 1:
            answer.append(i[0][0])
        else:
            answer.append(i[0][0])
            answer.append(i[1][0])

    return answer