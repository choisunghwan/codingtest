import sys
from unicodedata import decimal
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

a = input()
stack = []
res=''

print(a)

for x in a:
    # 입력값 x 가 숫자라면
    if x.isdecimal():
        res += x
    # x가 숫자가 아니라면면
    else:
        if x == '(':
            stack.append(x)
        elif x=='*' or x =='/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(x)
        elif x =='+' or x=='-':
            while stack and stack[-1] !='(':
                res += stack.pop()
            
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] !='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)
