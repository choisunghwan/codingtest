import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt
n , limit = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
cnt = 0 #구명보트 개수

while p: #p가 비워져있으면 false
    if len(p) ==1:
        cnt+=1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt +=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1

print(cnt)

