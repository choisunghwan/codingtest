import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

def DFS(L):
    global cnt
    if L==m: # L == m(2) , 문제에서 n은 2입니다.
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

if __name__ =="__main__":
    n,m = map(int,input().split()) # n:구슬 개수, m:뽑은 구슬 수
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)