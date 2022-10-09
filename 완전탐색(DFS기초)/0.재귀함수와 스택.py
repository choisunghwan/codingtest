import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

def DFS(x):
    if x>0:
        print(x)
        DFS(x-1)



if __name__ =="__main__":
    n = int(input())
    DFS(n)