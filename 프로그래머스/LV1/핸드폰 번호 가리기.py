def solution(phone_number):
    # 전화번호의 길이를 구한다.
    length = len(phone_number)
    
    # 뒷 4자리를 제외한 앞부분을 *로 대체한다.
    masked_part = '*' * (length-4)
    
    # 마지막 4자리를 추출합니다.
    last_part = phone_number[-4:]
    
    # 두 부분을 합쳐서 반환한다.
    return masked_part + last_part

# 예제 테스트
print(solution("01033334444"))  # 출력: *******4444
print(solution("027778888"))    # 출력: *****8888
