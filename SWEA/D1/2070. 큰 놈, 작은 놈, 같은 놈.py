import sys
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\SWEA\\D1\\input.txt", 'rt')


T = int(input()) # 테스트 케이스의 개수 

for Testcount in range(0, T):

    a, b = map(int,input().split()) # 2개의 수 입력받음.
    
    if a > b :
        print("#%d %s" %(Testcount+1,'>'))
    elif a < b:
        print("#%d %s" %(Testcount+1,'<'))
    else:
        print("#%d %s" %(Testcount+1,'='))