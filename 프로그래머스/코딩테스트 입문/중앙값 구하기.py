def solution(array):
    array.sort()
    
    print(array[0])
    # print(len(array))
    if len(array) % 2 == 0:
        print("짝수")
    elif len(array) % 2 != 0:
        temp = len(array) // 2 
        print(array[temp])
        return (array[temp])

