'''
2022-07-16
반복문(for, while


a = range(10) #range 함수는 0-9 까지 정수리스트
print(list(a))

a = range(1,10) # 1 - 9 까지 정수리스트 만듦
print(list(a))

for i in range(10): # i 는 0 - 9 까지 반복. 즉 총 10번 반복함.
    print("hello")
    print(i)


# 10부터 1씩 작아짐.
for i in range (10, 0, -1):
    print(i)


i = 1
while i <= 10:
    print(i)
    i = i + 1


i = 10
while i>=1:
    print(i)
    i = i-1

i = 1 
while True:
    print(i)
    if i == 10:
        break  # i 가 10 이되면 반복을 멈춘다.
    i+=1

for i in range( 1, 11):
    if i % 2 == 0:
        continue # i를 2로 나누었을때 나머지가 0인 짝수일때 그냥 넘어간다.
    print(i)
'''

for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:  #위 for 문이 5에서 break 당했기 때문에 else 출력되지 않는다.
    print(11)
