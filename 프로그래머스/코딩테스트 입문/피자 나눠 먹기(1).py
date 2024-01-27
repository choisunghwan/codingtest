

def solution(n):
    if n%7 == 0:
        return n//7 
    
    else:
        return n//7 + 1 
    

_list = [7, 1, 15]

for _ in _list:
    print(solution(_))