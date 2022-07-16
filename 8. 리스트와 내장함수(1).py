'''
 리스트와 내장함수(1)
'''

import random as r

# 빈 리스트
a = [] 
print(a)

b = list()
print(b)

# 리스트 초기화
a=[1,2,3,4,5]
print(a)
print(a[0])

b=list(range(1,11))
print(b)

#a 리스트 와 b 리스트 합쳐서 c에 담기
c=a+b
print(c)

# append() 이용해서 추가하기
print(a)
a.append(6)
print(a)

a.insert(3, 7) # 3번 인덱스에 7이 들어감
print(a)

a.pop() # 리스트 맨뒤 수를 뺀다.
print(a)
a.pop(3) #3번인덱스 값이 제거된다.
print(a)

a.remove(4) # 리스트에 4라는 값을 제거한다.
print(a)

print(a.index(5)) #index()함수는 5라는 값이 몇번 인덱스인지 인덱스 값을 알려준다.



a = list(range(1,11))
print(a)
print(sum(a)) #a라는 리스트 1-10까지 합한다.
print(max(a)) # a라는 리스트 중에 가장 큰 수(최댓값)
print(min(a)) # 가장 작은 수 (최솟값)

print(min(7,5)) # 7 과 5중 최솟값 출력 => 5

print(a)
r.shuffle(a) #shuffle()함수로 무작위로 섞는다.(랜덤모듈을 이용하여)
print(a)

#내림차순
a.sort(reverse=True)
print(a)

a.sort() # 오름차순
print(a)

#리스트 안 값 모두 제거
a.clear()
print(a)