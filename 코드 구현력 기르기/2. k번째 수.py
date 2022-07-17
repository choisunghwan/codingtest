import sys
#sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') #read text :rt

T = int(input())

for t in range(T):
    n, s, e, k = map(int,input().split())
    a = list(map(int,input().split()))
    #print(a[1:5]) 1~4번째 인덱스 추출
    a = a[s-1:e]
    a.sort() #오름차순 정렬
    print("#%d %d" %(t+1, a[k-1])) # k 번째 수를 추출하기위해 인덱스로는 k-1로 해야함.
