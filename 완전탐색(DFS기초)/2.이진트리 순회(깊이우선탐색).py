import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

def DFS(v):
    if v>7:
        return
    else:
        print(v, end=" ")
        DFS(v*2)
        DFS(v*2+1)
        

if __name__=="__main__":
    DFS(1)