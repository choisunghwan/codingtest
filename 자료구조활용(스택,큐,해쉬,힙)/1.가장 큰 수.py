import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

nums, m = map(int,input().split())

nums = list(map(int, str(nums))) #입력값 nums를 문자화 시켜서 하나하나 접근 가능하게 만듦 (5776 => 5,7,7,6) 그후 숫자화(int)시킴
stack=[]  #빈 리스트 생성(스택을 나타낼)



# 스택이 비어있지 않고, m이 0보다 크면서 stack의 맨마지막 수가 x보다 작다면 => 마지막 수를 pop(뺀다)
for x in nums:
    while stack and m>0 and stack[-1] < x: #stack변수(리스트)가 비어있으면 거짓, 비어있지 않으면 참  //// stack[-1] : stack에 맨 마지막 수를 의미
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[: -m]   # -m-1 까지 만 stack에 저장. 
    # ex) m이 2라면 .. 5 7 7 6 에서 -1은 6 //-2는 7 //-3은 7 이다. []: -m]은 m-1까지니까 5 7 까지 출력됨

for x in stack:
    print(x , end='')