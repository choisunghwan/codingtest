def solution(numbers):
    temp = 0
    # for i in numbers:
        # temp += i
    
    answer = sum(numbers) / len(numbers)
    return answer

numbers = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]
for i in numbers:
    print(solution(i))