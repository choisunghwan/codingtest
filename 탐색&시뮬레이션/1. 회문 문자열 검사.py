import sys
#sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')
n = int(input()) # 입력 받을 문자열 데이터 N개


for i in range(n): # n 번 반복한다.
    s = input()
    s = s.upper() #S 문자열을 전체 대문자로 만들어준다.
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
    
    
    
    
    

    # size = len(s)

    # for j in range(size//2):
    #     if s[j] != s[-1-j]:
    #         print("#%d No" %(i+1))
    #         break
        
    # else:
    #     print("#%d YES" %(i+1))
