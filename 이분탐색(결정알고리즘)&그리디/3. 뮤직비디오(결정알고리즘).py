import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

def count(capacity):
    cnt = 1
    sum = 0
    for x in music:
        if sum + x > capacity:
            cnt+=1
            sum = x
        else:
            sum +=x
    return cnt

n, m = map(int,input().split()) #dvd에는 총 n곡이 들어감. m개의 dvd에 모든 영상을 녹화
music = list(map(int,input().split())) # 라이브에서 순서대로 부른 곡의 길이(분 단위)
maxx = max(music)
lt = 1
rt = sum(music)
res =0

while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and count(mid) <= m:
        res = mid
        rt = mid -1
    else:
        lt = mid + 1
print(res)
