import sys
#sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') #read text :rt

n, k =map(int,input().split())
a = list(map(int,input().split()))

res=set() #set() 자료구조는 중복을 제거해준다.

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m]) #set 자료구조에서는 append 가 아닌 add 이다.
res = list(res) # set 자료구조에는 sort(정렬)기능이 없다. 그러므로 다시 리스트화 시켜준다.

res.sort(reverse=True) # 내림차순 정렬 . 오름차순은 그냥 .sort()
print(res[k-1]) # 0부터 시작하므로 -1 해준다.