import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

def DFS(L, sum):
    global res
    if L > res:
        return
    if sum > m:
        return # 함수를 종료시켜라 명령도 함.
    if sum == m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__ =="__main__":
    n=int(input()) #동전 종류 개수
    a=list(map(int, input().split())) # n개의 동전 종류
    m=int(input()) #거스름돈
    res=2147000000
    a.sort(reverse=True) #오름차순이 아닌 내림차순으로..
    DFS(0,0)
    print(res)