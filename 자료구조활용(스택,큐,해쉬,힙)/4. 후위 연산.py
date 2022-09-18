import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x =='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x =='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x =='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)            
        elif x =='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])