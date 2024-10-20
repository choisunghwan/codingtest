num_list = [4, 2, 6, 1, 7, 6]

def solution(num_list):
    # print(num_list);
    a = 0;
    b = 0;
    
    for index , value in enumerate(num_list):
        
        # 짝수 번째 원소들의 합 
        if index % 2 == 0:
            a += value
        # 홀수 번째 원소들의 합
        if index % 2 != 0:
            b += value
            
    print(a);
    print(b);
            
#     결과 값 크기 비교 
    if a > b:
        return a;
    if b > a:
        return b;
    if a == b:
        return a;
        
            
    
    
    answer = 0
    return answer

# 함수 호출 및 결과 출력
result = solution(num_list)
print("결과:", result)