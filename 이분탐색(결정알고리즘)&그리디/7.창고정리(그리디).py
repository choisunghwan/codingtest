import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

L = int(input())
a = list(map(int,input().split()))
m = int(input())

a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1] -=1
    a.sort()

print(a[L-1]-a[0])