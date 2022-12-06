def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        # print(i) -> 0,1,2,3,4,5,6
        # print(arr) -> [1,1,3,3,0,1,1]
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer