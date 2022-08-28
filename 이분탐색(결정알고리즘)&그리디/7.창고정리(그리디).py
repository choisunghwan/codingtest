import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

L = int(input()) #가로의 길이
a = list(map(int,input().split())) # 각 열의 상자 높이
m = int(input()) # 높이조정 횟수

a.sort() # 오름차순 정렬을 해서 가장 높은곳, 가장 낮은곳 의 위치를 알아냄
for _ in range(m): # m 번 반복 (높이조정) 
    a[0]+=1   # a[0]은 가장 낮은 곳이기 때문에 1증가
    a[L-1] -=1 # 가장 높은 곳인 a[L-1]에서 1 감소
    a.sort() # 높이조정후 오름차순 정렬을 해준다.


# m 번의 높이조정이 끝나게 되면 문제에서 요구하는 가장 높은곳과 가장 낮은곳 차이를 구해준다.
print(a[L-1]-a[0])