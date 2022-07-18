import sys
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') 

n = int(input())
a = list(map(int, input().split())) # N명의 학생의 수학 성적 입력받음 
avg=sum(a)/n
#반올림 해주기. round()함수를 사용하지 않은 이유는 4.5 인경우 round 함수를 사용하면 4가 된다. round_half_even(짝수)방식임.
avg = avg + 0.5 # 그래서 0.5 를 더해줌으로써 0.5 이상인 경우 자릿수가 올라가기 때문에 소수점만 때주면(정수형으로 변경하면) 반올림이 된다.
avg = int(avg) 


min = 2147000000
for index, x in enumerate(a): #enumerate 를 사용하면 리스트의 인덱스, 값을 각각 저장해줌.
    tmp=abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res=index+1
    elif tmp == min:
        if x > score:
            score = x
            res = index + 1

print(avg, res)

