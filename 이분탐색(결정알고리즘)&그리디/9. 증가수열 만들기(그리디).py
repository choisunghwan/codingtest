import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

n = int(input())
a = list(map(int,input().split()))

lt = 0
rt = n - 1
last = 0
res = "" #res 를 문자열로 초기화
tmp = [] # 빈 리스트 

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt],'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
