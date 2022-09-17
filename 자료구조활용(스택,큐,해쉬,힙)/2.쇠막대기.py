import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

s = input()
stack =[]  #스택이라는 빈리스트 생성
cnt = 0 # 카운트 수를 담는 변수

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else: # 닫는 괄호라면?
        if s[i-1] == '(':
            stack.pop()
            cnt += len(stack) #스택의 길이를 cnt에 누적
        else:
            stack.pop()
            cnt+=1
print(cnt)