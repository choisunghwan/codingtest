def solution(denum1, num1, denum2, num2):
    denum3 = denum1 * num2 + denum2 * num1
    num3 = num1 * num2            

    for i in range(1, denum3 + 1):
        if (num3 % i == 0) & (denum3 % i == 0):
            gcd = i

    answer = [denum3/gcd, num3/gcd]

    return answer




import math
def solution(numer1, denom1, numer2, denom2):
    A_denom = denom1*denom2
    B_numer = (denom1*numer2)+(denom2*numer1)
    
    gcd = math.gcd(A_denom,B_numer)
    A_denom = A_denom//gcd
    B_numer = B_numer//gcd

    answer = [B_numer,A_denom]
    
    return answer