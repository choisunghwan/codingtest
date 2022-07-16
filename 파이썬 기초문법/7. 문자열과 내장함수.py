'''
2022-07-16

문자열과 내장함수
'''

msg = "it is Time"
print(msg.upper()) # upper()함수는 모든 문자를 대문자로 변환해줌.
print(msg.lower()) # lower()함수는 소문자화 시켜준다.
print(msg) # 그러나 msg 변수의 값이 변하지는 않는다.

tmp = msg.upper()
print(tmp)

print(tmp.find('T')) # tmp 변수안의 T의 인덱스 번호 리턴해줌.
print(tmp.count('T')) # tmp 안에 문자T의 개수를 출력해줌.

print(msg[:2]) #슬라이스 . 문자열 첫번째부터 0 1 번만 출력
print(msg[3:5]) # 3번 인덱스 -4번인덱스 의 msg 값 출력

print(len(msg)) # 길이 출력(이때 공백 포함)


#문자 한개 한개 씩 접근
for i in range(len(msg)):
    print(msg[i], end='')
print()

for x in msg:
    print(x , end='')
print()

#대문자만 출력 : isupper
for x in msg:
    if x.isupper(): #isupper()은 대문자 라면 참. 소문자이면 거짓
        print(x, end=' ')
print()

#소문자만 출력 : islower
for x in msg:
    if x.islower():
        print(x, end=' ')
print()

# 알파벳 만 출력
for x in msg:
    if x.isalpha():  #isalpha()는 알파벳일 경우 참. 아니면 거짓
        print(x, end='')
print()


# 문자를 아스키 넘버로 출력하기
tmp='AZ'
for x in tmp:
    print(ord(x)) #ord()는 아스키 넘버 출력 // 참고로 A:65 Z:90이다.

tmp='az'
for x in tmp:
    print(ord(x)) 

# 아스키 넘버를 문자로 출력하기.
tmp = 65
print(chr(tmp)) 