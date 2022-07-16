'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수 출력하기
'''

#1 내가 푼 방식.
n = int(input())
for i in range (1, n+1):
    if i % 2 == 0:
        continue
    print(i)

#1 다른 방식
n = int(input())
for i in range (1, n+1):
    if i % 2 == 1:
         print(i)


#2
sum = 0
n = int(input())
for i in range(1, n + 1):
    sum += i    #sum = sum + i 와 같다.
print(sum)

#3

n = int(input())
for i in range(1,n+1):
    if n % i ==0:
        print(i , end=' ') #end를 써주면 줄바꿈 없이 한줄에 출력된다.


