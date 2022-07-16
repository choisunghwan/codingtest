'''
2022-07-16
중첩 반복문(2중 for문)
'''
'''
for i in range(5): #0-4까지 5번 반복
    for j in range(5):
        print(j, end=' ')
'''


'''
#좀 더 한눈에 보기 쉽게
# 즉, i 가 0 일때 j는 0-4 출력 . i 가 1일때 j는 0-4 출력. 이렇게 게속 반복
for i in range(5):
    print('i:',i ,sep='',end=' ')
    for j in range(5):
        print('j:',j,sep='',end=' ')
    print()
'''


'''
#별 5개씩 5줄 출력하기
for i in range(5):
    for j in range(5):
        print("*",end=' ')
    print()
'''

'''
# 계단식 별 출력하기.
for i in range(5):
    for j in range(i+1):
        print("*",end=' ')
    print()
'''

# 반대로 계단별
for i in range(5):
    for j in range(5-i):
         print("*", end=' ')
    print()