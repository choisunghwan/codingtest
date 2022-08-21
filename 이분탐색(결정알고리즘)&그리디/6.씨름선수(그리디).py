import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

n = int(input()) #지원자 수 

body= []

for i in range(n): #지원자 수(n)번 반복한다.
    h,w = map(int,input().split()) #키, 몸무게를 입력받아서
    body.append((h,w)) # 튜플 형태로 키(h) 와 몸무게(w)를 body리스트에 추가해준다.

body.sort(reverse=True) #내림차순 정렬  | 오름차순 : body.sort()

largest = 0
cnt = 0

for x , y in body: #x:키 y:몸무게
    if y > largest: #몸무게y가 최고 값(largest)보다 크다면
        largest = y #저장
        cnt +=1 # cnt 1증가
print(cnt) # 선발된 인원 출력
