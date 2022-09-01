import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

p ,k = map(int,input().split()) #주어진 번호 k
cnt = 0 # 카운트 변수

for _ in range(k, p+1):
    cnt +=1
print(cnt)
    