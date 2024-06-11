def solution(nums):
    # 포켓몬의 종류이 수를 센다.
    unique_types = len(set(nums))
    # 선택할 수 있는 최대 마리의 수는 N/2 입니다.
    max_selectable = len(nums)/2
    
    # 최대로 선택할 수 있는 포켓몬 종류의 수를 반환합니다.
    return min(unique_types,max_selectable)
    
    # 예제 테스트
print(solution([3, 1, 2, 3]))  # 출력: 2
print(solution([3, 3, 3, 2, 2, 4]))  # 출력: 3
print(solution([3, 3, 3, 2, 2, 2]))  # 출력: 2