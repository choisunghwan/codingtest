import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

def Count(len):
    cnt = 0
    for x in line:
        cnt +=(x//len)
    return cnt

k, n = map(int,input().split()) # 이미 가지고 있는 랜선의 개수 k , 필요한 랜선의 개수 n
line = []
res = 0
largest = 0 

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
