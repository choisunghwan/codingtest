import sys
sys.stdin = open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D2\\input.txt", 'rt')
T = int(input())
for test_case in range(1,T+1):
    s = input() # 문자 받기 koreakorea...
    for j in range(1,10): # 0-9
        if s[:j] == s[j:j*2]:
            
            print("#{} {}".format(test_case,j))
            break

