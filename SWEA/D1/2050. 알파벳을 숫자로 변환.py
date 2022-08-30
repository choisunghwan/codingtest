import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

k = list(input()) # 변수 k에 입력받은 리스트 저장
for i in range(len(k)): # 변수 k 길이 만큼 반복
    print(ord(k[i])-64, end=' ') # ord(): 특정문자를 아스키 코드값으로 변환해주는 함수이다. \\ end=' ' :띄어 쓰기
    # -64를 하는 이유는 아스키 코드 값으로 A : 65 이다.
    