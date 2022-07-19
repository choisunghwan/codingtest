import sys
# sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt')

n = int(input()) # 주사위 게임에 참여하는 사람이 수 
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c =map(int, tmp) # tmp에 있는 문자가 숫자로 매핑되어서 a, b, c에 저장됨.
    if a == b and b == c:   # 가장 큰 값을 맨위 if 로 정해야됨. 왜냐하면 문제에서 가장 많은 상금을 받은 사람의 상금을 출력하라고 하였고, 만약 작은값을 우선으로 둔다면 true로 해석하고 아래 코드 실행하지 않기 때문
        money = 10000 + a * 1000  # 규칙 1 : 같은 눈이 3개 나오면
    elif a == b or a == c:
        money = 1000 + a * 100 # 규칙 2 : 같은 눈이 2개 나오면 (+ 상금(money)계산 할때 편하게 하기 위해서 or b==c를 한줄에 써버리게 되면 규칙 적용 어려움)
    elif b == c:
        money = 1000 + b * 100 # 규칙 3 : 같은 눈이 2개 나오면
    else:
        money = c * 100 # 규칙 4 : 같은 눈이 1개 나오면
    if money > res: # res 를 기준으로 n명의 참가자 상금 비교 
        res = money
print (res)