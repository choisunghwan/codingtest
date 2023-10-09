def solution(name, yearning, photo):
    dict = {}
    for n, y in zip(name, yearning):
        dict[n] = y
    print(dict)
    
    answer = []
    for i in photo:
        temp=0
        for j in i:
            # print(dict.get(j,0))
            temp+= dict.get(j,0)
        answer.append(temp)
    
    return answer