'''
리스트와 내장함수(2)
'''

a=[23, 12, 36, 53, 19]

print(a[:3]) # 0번 인덱스 ~ 2번 인덱스 까지 출력 | 슬라이스(부분 출력)
print(a[1:4]) # 1번 인덱스 ~3번 인덱스 까지 출력
print(len(a)) # 길이 출력

#리스트 값을 하나씩 접근/출력하기

for i in range(len(a)):
    print(a[i],end=' ')
print()


for x in a:
    print(x,end=' ')
print()


for x in a:
    if x % 2 == 1:
        print(x,end=' ')
print()



#튜플은 값을 변경할수 없다.
'''
b=(1,2,3,4,5)
print(b[0])
b[0]=7
print(b[0])
'''

#리스트는 값 변경 가능.
b=[1,2,3,4,5]
print(b[0])
b[0]=7
print(b[0])

print()

#enumerate() 사용

for x in enumerate(a): # 인덱스와 함께 리스트 값 출력
    print(x)
print()
for x in enumerate(a): # 인덱스와 함께 리스트 값 출력
    print(x[0],x[1])
print()
for index , value in enumerate(a):
    print(index,value)
print()


# all()함수 . a리스트 를 하나씩 x에 접근 하는데 60보다 작은지 !
if all(60 > x for x in a): # 모두 참인 경우에만 참. 하나라도 거짓이 있다면 거짓.
    print("YES")
else:
    print("NO")

print()

# any()함수
if any(15 > x for x in a): # any()는 하나라도 참이 되는게 있으면 참이다. 모두 거짓일때만 거짓.
    print("YES")
else:
    print("NO")