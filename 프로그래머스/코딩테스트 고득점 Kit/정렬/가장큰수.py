def solution(numbers):
    # Step 1: numbers 리스트의 각 요소를 문자열로 변환하여 str_numbers 리스트 생성
    str_numbers = list(map(str, numbers))
    
    # Step 2: 문자열로 변환된 리스트를 특정 기준으로 정렬
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    # Step 3: 정렬된 문자열 리스트를 하나의 문자열로 이어붙입니다.
    answer = ''.join(str_numbers)
    
    # Step 4: 결과 문자열이 '0'으로 시작하면 '0'을 반환합니다.
    return answer if answer[0] != '0' else '0'

# 예제 테스트
print(solution([6, 10, 2]))  # "6210"
print(solution([3, 30, 34, 5, 9]))  # "9534330"
