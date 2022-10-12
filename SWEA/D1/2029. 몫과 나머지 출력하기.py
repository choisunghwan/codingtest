import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

T = int(input())

for test_case in range(1,T + 1): # T만큼 반복한다.
    n, m = map(int, input().split())
    print("#%d" %test_case, end=' ')
    print(n//m, end=' ')
    print(n%m)
