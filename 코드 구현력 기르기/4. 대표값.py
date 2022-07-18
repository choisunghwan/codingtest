import sys
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') 

n = int(input())
a = list(map(int, input().split())) # N명의 학생의 수학 성적 입력받음 
avg=round(sum(a)/n)
min = 2147000000
for index, x in enumerate(a): #enumerate 를 사용하면 리스트의 인덱스, 값을 각각 저장해줌.
    tmp=abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res=index+1
    elif tmp == min:
        if x > score:
            score = X
            res = index + 1

print(avg, res)


1