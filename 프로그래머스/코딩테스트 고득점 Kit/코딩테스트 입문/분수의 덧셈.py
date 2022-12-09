def solution(denum1, num1, denum2, num2):
    denum3 = denum1 * num2 + denum2 * num1
    num3 = num1 * num2            

    for i in range(1, denum3 + 1):
        if (num3 % i == 0) & (denum3 % i == 0):
            gcd = i

    answer = [denum3/gcd, num3/gcd]

    return answer