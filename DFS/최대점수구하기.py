import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\DFS\\input.txt","r")

def DFS(L, sum, time):   # L: 1번 2번.. sum: 점수 , time: 시간
    global res
    if time > m: # 제한 시간을 초과한 경우
        return

    if L == n: # 모든 문제를 확인한 경우
        if sum > res:
            res = sum
        return
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__ == "__main__":
    n, m = map(int,input().split()) #n:문제 개수 , m: 제한시간
    pv = [] # 문제 점수 (리스트)
    pt = [] # 문제 시간 (리스트)

    for i in range(n):
        a, b = map(int,input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000  #res 변수는 답이 될 변수이기 때문에 가장 작은수로 설정

    DFS(0, 0 ,0)

print(res)

