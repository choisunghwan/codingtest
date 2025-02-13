import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')
# input.txt : 9977252641 5


num, m =map(int,input().split())
print("num , m :", num,m)


num = list(map(int, str(num)))
print("num : " , num)

stack = []
for x in num:
    print(x)
    while stack and m > 0 and x > stack[-1]:
        stack.pop()
        m-=1
    stack.append(x)

if m != 0:
    stack = stack[:-2]

# 출력방법1:  res = ''.join(map(str,stack))
# print(res)

# 출력방법2
for x in stack:
    print(x,end='')