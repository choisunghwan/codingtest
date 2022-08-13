import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

n, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort() #숫자들을 오름차순으로 정렬시킨다.
lt = 0  # 맨 왼쪽 값을 0으로 
rt = n-1 # 맨 오른쪽 값을 n-1 으로 (why?: 인덱스값은 0부터 시작하기때문에)

while lt <= rt:
    mid = (lt + rt)// 2
    if nums[mid] == m:
        print (mid+1)
        break
    elif nums[mid] > m:
        rt = mid - 1 
    else:
        lt = mid + 1


