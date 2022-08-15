import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

def count(len):
    cnt = 1
    EndPoint = line[0]
    for i in range(1,n):
        if line[i] - EndPoint >= len:
            cnt += 1
            EndPoint = line[i]
    return cnt

n, c = map(int,input().split())

line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)
line.sort()
lt = 1
rt = line[n-1]

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)

