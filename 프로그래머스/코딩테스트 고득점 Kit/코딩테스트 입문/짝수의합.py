def solution(n):
    answer = 0

    for num in range(n+1):
        # print(num)
        if num % 2 ==0: #만약 n 이 짝수라면
            answer+=num

    return answer