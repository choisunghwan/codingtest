def solution(numbers, target):
    answer = 0 # 타켓 넘버를 만들 수 있는 방법의 수를 저장하는 변수

# dfs 함수는 현재 숫자의 인덱스(index)와 현재까지의 합(current_sum)을 받아 재귀적으로 호출됩니다.
    def dfs(index, current_sum):
        # nonlocal answer 은 내부함수인 dfs에서 바깥 함수의 변수 answer를 수정할 수 있게 해줌.
        # 이게 없으면 answer는 함수 내부에서 로컬 변수로 인식됩니다.
        nonlocal answer  

        # 모든 숫자를 처리한 경우

        #**if index == len(numbers):**는 현재 index가 numbers 배열의 끝에 도달했는지 확인합니다. 
        # 배열의 모든 숫자를 다 처리했다는 의미입니다.
        if index == len(numbers): 
            if current_sum == target:
                answer += 1

            # 그 후에는 **return**으로 함수가 종료됩니다. 더 이상 계산할 숫자가 없기 때문입니다.
            return
        

        # 현재 숫자를 더하는 경우
        dfs(index + 1, current_sum + numbers[index])

        # 현재 숫자를 빼는 경우
        dfs(index +1,current_sum - numbers[index])
    
    # 탐색 시작
    #초기 호출: 첫 번째 숫자부터 탐색을 시작해야 하므로 dfs(0, 0)을 호출합니다. 여기서 0은 처음 인덱스이고, 두 번째 0은 현재 합계입니다. 
    # 즉, 아무 숫자도 아직 더하거나 빼지 않은 상태에서 시작합니다.
    dfs(0, 0)


    #모든 탐색이 완료되면, answer 값(타겟 넘버를 만드는 방법의 수)을 반환합니다.
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3

result = solution(numbers, target)
print(result) # 출력: 5