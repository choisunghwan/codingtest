import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

n = int(input()) # 숫자를 입력받음.
res = 0
for i in range(1, n+1):
    res += i 
print(res)