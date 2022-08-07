import sys
import math
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\SWEA\\D1\\input.txt", 'rt')


T = int(input())  # 테스트케이스의 개수 T
for testcount in range(1, T+1):  # 테스트 케이스 반복
    res = 0
    nums = list(map(int, input().split()))  # 숫자 입력받음.

    for i in nums: #입력 받은 수를 하나씩 i에 넣으면서 반복
        res += i #i를 res에 누적 합
    print("#%d %d" % (testcount, round(res/len(nums))))
