import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

n = int(input()) # 1개의 정수가 주어진다.
res=0

for i in range(n):
    res= 2**(i+1)
    print(res, end=' ')