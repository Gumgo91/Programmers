def solution(new_id):
    
    newid = new_id.lower()
    
    answer = ''
    for s in newid:
        if ('a'<=s and s<='z') or ('0'<=s and s<='9') or s=='-' or s=='_':
            answer = answer + s
        elif s=='.':
            if answer!='':
                if answer[-1]!='.':
                    answer = answer + s
    
    if answer!='': 
        if answer[0]=='.':
            answer = answer[1:]
    if answer!='':    
        if answer[-1]=='.':
            answer = answer[:-1]
    
    if answer == '':
        answer = 'a'
        
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
            
    if len(answer)==1:
        answer = answer + answer + answer
    elif len(answer)==2:
        answer = answer + answer[-1]
    
    return answer