import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

def DFS(x):
    if x == 0:
        return # 함수를 종료시켜라 명령도 함.
    else:

        DFS(x//2) # 재귀 호출. n 을 2로 나눈 몫
        print(x % 2, end=' ')  # n을 2로 나눈 나머지




if __name__ =="__main__":
    n = int(input())
    DFS(n)