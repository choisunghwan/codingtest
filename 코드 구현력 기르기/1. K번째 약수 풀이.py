import sys
# sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') #read text :rt

n, k = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    if n % i == 0:
        cnt +=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)