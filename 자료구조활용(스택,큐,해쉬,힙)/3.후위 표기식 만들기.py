import sys
from unicodedata import decimal
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

a = input() # 입력받은 중위식 a 변수에 저장
stack =[] # 빈리스트 만들기
res =''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1]== '*' or stack[-1]=='/'): #스택이 비워져있지 않고, 스택의 맨 상단이
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] !='(':  #stack이 비워질때 까지 반복
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1]!='(':
                res += stack.pop()
            stack.pop()
while stack : #stack 비어있을때 까지 반복함.
    res+=stack.pop()
print(res)