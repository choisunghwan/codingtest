'''
2022-07-16

변수입력과 연산자 
'''
# input()을 이용한 입력
'''
a = input(" 아무거나 입력하세요: ")
print(a)
'''

# .split()는 입력 받은 값을 띄어쓰기로 분리시켜 입력받는다.
'''
a, b = input("숫자를 입력하세요: ").split() 
print(a+b)
c = a + b
print(type(c))
'''
# 문자형인 a 와 b 를 숫자로 바꿔준다. 
'''
a = int(a)
b = int(b)
print(a+b)
print(type(a))
'''
# str 을 int 형으로 바꾸는 map 함수!
a, b = map(int, input("숫자를 입력하세요: ").split())
print(a + b) # 더하기
print(a - b) # 빼기
print(a * b) # 곱하기
print(a / b) # 나누기
print(a // b) # 몫
print(a % b) # 나머지
print(a ** b) # 거듭제곱


# 실수와 정수 가 계산되면 실수형이다.(float)
a = 4.3
b = 5
c = a + b
print(type(c)) 