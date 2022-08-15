import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\이분탐색(결정알고리즘)&그리디\\input.txt",'rt') #read text :rt

n = int(input()) #회의의 수

meeting = []
for i in range(n):
    s , e = map(int,input().split()) #회의시작 (s) , 회의 끝(e)
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1], x[0]))
et = 0
cnt =0
for s,e in meeting:
    if s>=et:
        et = e
        cnt +=1
print(cnt)
