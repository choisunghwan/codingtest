import sys
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\SWEA\\D2\\input.txt", 'rt')

n = int(input()) # 1개의 정수가 주어진다.

for i in range(1, n+1): # 1~100
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i , end=" ")
    else:
        print("-" * clap, end=" ")

