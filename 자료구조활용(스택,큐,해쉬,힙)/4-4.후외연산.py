import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

a = input()
print(a)

stack = []
res = ''

for x in a:
    # x가 숫자일 경우
    if x.isdecimal():
        stack.append(int(x))
    # x가 숫자가 아닐 경우
    else:
        if x =='+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x =='-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print(stack[0])    

