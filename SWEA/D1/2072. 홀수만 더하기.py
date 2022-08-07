import sys
from tkinter import N
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

T = int(input()) # 테스트 케이스의 개수 T


for testcount in range(T) : #테스트 케이스 수만큼
    nums = list(map(int,input().split())) # 10개의 수 입력
    res = 0
    for i in nums:
        if i % 2 ==1:
            res +=i

    print('#%d %d' % (testcount+1, res))

#res = sum(n for n in nums if n%2==1) 
#print( f"#{testcount} {res}" )