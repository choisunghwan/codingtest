import sys
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt')

def reverse(x): #뒤집는 함수
    res = 0
    while x > 0:
        t = x % 10 # x의 1의자릿수 가 t에 저장됨.
        res = res * 10 + t
        x = x // 10
    return res



def isPrime(x): # 소수인지 확인하는 함수
    if x == 1:
        return False
    for i in range (2, x//2+1):
        if x % i == 0: 
            return False #약수가 발견되는 False를 리턴해주면서 종료
    else:
        return True


n = int(input())
a = list(map(int, input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')







