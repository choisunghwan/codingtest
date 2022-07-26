import sys
#sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

n , m = map(int,input().split()) # N(수열 개수) , M(i번째부터 j번째 수의 합)

a = list(map(int,input().split())) # 수열 리스트로 받기

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot +=a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)