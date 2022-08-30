import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 달마다 마지막 날 

T = int(input()) #테스트 케이스 개수 입력
for testcase in range(T): # 테스트 케이스 개수 만큼 반복한다.
    s = input()
    month = int(s[4:6]) # s를 4부터 5까지 자름.
    day = int(s[6:8]) # 6부터 7까지 다름
    res = "-1" #res 변수에 -1 초기화.

    #만약 1보다 같거나 크고 12보다 작거나 같다 AND day가 md리스트 보다 같거나 작다
    if 1<=month and month<=12 and 1<=day and day<=md[month-1]:
        #res 에 0부터 3까지 자름 + 4부터 5까지 자름 / 6부터 7까지 자름
        res = s[0:4]+"/"+s[4:6]+"/"+s[6:8]
    #출력 
    print( f"#{testcase+1} {res}" )