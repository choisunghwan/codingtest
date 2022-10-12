import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')

a, b = map(int, input().split()) # 입력 a,b



if (a == 1 and b ==2) or (a == 2 and b == 3) or (a == 3 and b ==1):
    print("B")
else:
    print("A")

