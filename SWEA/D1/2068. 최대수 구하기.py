import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

T = int(input()) #테스트 케이스의 개수

for testcount in range (T):
    a = list(map(int,input().split()))
    print("#%d %d" %(testcount+1, max(a)))
    
