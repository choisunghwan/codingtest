import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

n = int(input()) #지원자 수 

body= []

for i in range(n): #5번 반복한다.
    h,w = map(int,input().split()) #키, 몸무게 
    body.append((h,w))
body.sort(reverse=True) #내림차순 정렬

largest = 0
cnt = 0

for x , y in body:
    if y > largest:
        largest = y
        cnt +=1
print(cnt)
