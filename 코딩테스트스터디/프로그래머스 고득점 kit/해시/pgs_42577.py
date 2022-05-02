def solution(phone_book):
    
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]): #str 의 starts with 사용해 접두사 탐색
            answer = False
    
    return answer