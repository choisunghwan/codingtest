'''
2022-07-16
조건문 if(분기, 중첩)
'''
x = 7
if x == 7: 
    print("x 는 7 이 맞습니다.")

if x != 7:
    print("x 는 7 이 아닙니다.")

    
x = 15

if x >= 10:
    if x % 2 == 1:
        print("x는 10이상의 홀수입니다.")


# if 중첩
x = 9

if x > 0:
    if x < 10:
        print("x는 10보다 작은 자연수 ")
# and 연산자 사용
x = 7
if x > 0 and x < 10:
    print("x는 10보다 작은 자연수 입니다.")
# a < x < c 사용
x =7 
if 0 < x < 10 :
    print (" x는 10 보다 작은 자연수 입니다.")


# if , else 사용
x = 10
if x > 0:
    print("양수")
else:
    print("음수")

x = 93
if x >= 90:
    print("A")
elif x >= 80:
    print("b")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")