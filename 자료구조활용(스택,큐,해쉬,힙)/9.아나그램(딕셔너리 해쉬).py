import sys
from collections import deque
# 입력 값
# AbaAeCe
# baeeACA
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

#입력받기
a = input()
b = input()

#각 문자열의 문자 개수를 저장할 딕셔너리 생성
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x,0) + 1
# print(str1)

for x in b:
    str2[x] = str2.get(x,0) + 1
# print(str2)

for i in str1.keys():
    # str1 의 키 값이 str2에 있는지 확인.
    if i in str2.keys():
        # 같은 문자라도 개수가 다르면 애너그램이 아님.
        if str1[i] != str2[i]:
            print("NO")
            break
    #문자가 아예 없을 경우
    else:
        print("NO")
        break
# 모든 문자가 일치할 경우 
else:
    print("YES")



# print(str2)

