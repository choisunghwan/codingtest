def solution(money):
    coffee = money // 5500
    left = money % 5500
    answer = [coffee,left]
    return answer


for i in [5500,15000]:
    print(solution(i))