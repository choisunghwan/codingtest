def solution(s):
    balance = 0 #열린 괄호와 닫힌 괄호의 균형을 나타내는 카운터
    
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        if balance < 0 :
            return False;
        
       # 모든 괄호를 검사한 후 balance가 0이어야 올바른 괄호 문자열
    return balance == 0