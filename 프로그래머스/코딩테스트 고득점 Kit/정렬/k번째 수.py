#array: [1,5,2,6,3,7,4] 입력됨.
#command: [[2,5,3],[4,4,1],[1,7,3]] 입력됨.

# i = 2, j = 5, k =3 이라고 한다면
#(즉, command 안의 수를 가르키는 변수)


def solution(array, commands):
    answer = []
    #ex: 배열의 2~5번째 자르기위해서는 slice를 사용..? 해야할듯. 
    #인덱스는 0부터 시작한다는점 유의.
    for i in range(len(commands)):
        arr = array[commands[i][0]-1 : commands[i][1]] # 2번째 부터 5번째
        arr.sort() # 오름차순 정렬
        answer.append(arr[commands[i][2]-1])
        
    return answer
