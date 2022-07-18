import sys
# sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') 
n = int(input()) # N개의 자연수의 개수 입력

a = list(map(int,input().split())) # N개의 자연수 입력

#수의 자릿수의 합 더하는 함수.
def digit_sum(x):
    sum = 0
    #while x > 0:
    #    sum += x % 10
    #    x = x // 10
    #return sum
    for i in str(x):
        sum+=int(i)
    return sum


max = -2147000000 

# 자릿수의 합 중에서 가장 큰 값 출력
for x in a:
    tot=digit_sum(x)
    if tot > max:
        max = tot
        res = x

print (res)



