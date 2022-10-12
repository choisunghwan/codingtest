import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

n = input()
for i in n:
    ans = ord(i)-64 #ord()함수는 유니코드 문자에 대응되는 정수를 표현.
    # 대문자 A:65
    print(ans, end=" ")