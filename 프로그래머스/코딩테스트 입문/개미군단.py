def solution(hp):
    answer = 0
    answer = (hp // 5) + ((hp % 5) // 3) + (((hp % 5) % 3) // 1)
    return answer

# 장군개미: 공격력 5
# 병정개미: 공격력 3
# 일개미: 공격력 1

# 체력 23여치 사냥 
