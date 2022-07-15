''' 
변수명 정하기
 1) 영문과 숫자, _로 이루어진다.
 2) 대소문자를 구분한다
 3) 문자나, _ 로 시작한다.
 4) 특수문자를 사용하면 안된다. (&,% 등)
 5) 키워드를 사용하면 안된다. (if, for 등)
'''
a = 1
A = 2
A1 = 3
# 2b = 4  입력시 에러 발생.   위 3) 참고.
print (a, A, A1)

# 한꺼번에 여러개의 변수를 설정하고 출력할 수 있다.
a, b, c =3, 2, 1
print(a,b,c)

# 값 교환
a, b = 10, 20
print (a, b)
a, b = b, a
print (a, b)

# 변수 타입
a = 12345
print(type(a))

a = 12.12345
print(type(a))

a = "student"
print(type(a))

# 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number :",a, b, c)

# 줄바꿈 설정 방식 ( <sep=''> || <end=''> )

print(a,b,c,sep=', ') # sep는 각 값을 분리할때 설정
print(a, b, c, sep='')
print(a, b, c, sep='\n')

print(a, end='') #a를 출력한후 자동 줄바꿈을 하기 싫을때 end 를 이용함.
print(b, end='')
print(c)
# END