def fac(num):
    a = 1
    for i in range(1,num+1):
        a *= i
    return a

def solution(balls, share):
    answer = 0
    n = fac(balls)
    m = fac(share)
    nm = fac(balls-share)
    
    answer = n / (nm*m)
    return answer