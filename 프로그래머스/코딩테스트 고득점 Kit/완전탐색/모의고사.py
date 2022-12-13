def solution(answers):
    answer = []
    
    #각 학생이 찍는 반복되는 번호 구간만 각 변수에 저장합니다.
    student_1 = [1, 2, 3, 4, 5] #5개가 반복됨
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5] #8개 반복됨
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개 반복됨
    
    # 문제의 '제한조건' 에 시험문제는 최대 10,000개로 구성되어있다고 하였으므로, 각 학생의 반복횟수를 파악하여 변수에 저장합니다.
    student_count_1 = int(10000 / len(student_1))
    student_count_2 = int(10000 / len(student_2))
    student_count_3 = int(10000 / len(student_3))
    
    #5개가 반복되는 1번 수포자는 총 시험문제가 10,000개 이므로 10,000/5 로 2000번 곱해주어야함.
    #print(student_count_1) 
    
    student_1 = student_1 * student_count_1
    student_2 = student_2 * student_count_2
    student_3 = student_3 * student_count_3
    
    # 변수 값 0으로 선언
    index = 0
    result_count_1 = 0
    result_count_2 = 0
    result_count_3 = 0
    
    for i in answers:
        if i == student_1[index]:
            result_count_1 += 1
        if i == student_2[index]:
            result_count_2 += 1
        if i == student_3[index]:
            result_count_3 += 1
        index += 1
    
    result_point = [result_count_1,result_count_2,result_count_3]
    
    if max(result_point) == result_point[0]:
        answer.append(1)
    if max(result_point) == result_point[1]:
        answer.append(2)
    if max(result_point) == result_point[2]:
        answer.append(3)
        
        
    return answer