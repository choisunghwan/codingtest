import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')
# input : ()(((()())(())()))(())  # 결과 : 17

s = input()
stack = []
cnt =0

for i in range(len(s)):
    #열린 괄호
    if s[i] =='(':
        stack.append(s[i])
    #닫는 괄호
    else:
        stack.pop()

        # 바로 앞이 열린 괄호일때
        if s[i-1] == '(':
            cnt += len(stack)
        # 바로 앞이 닫힌 괄호일때
        else:
            cnt+=1

print(cnt)