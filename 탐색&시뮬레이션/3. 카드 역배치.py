import sys
#sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

a = list(range(21))
for _ in range(10): #_(언더바): 변수가 없는것. 그냥 반복함
    s, e = map(int, input().split())
    for i in range((e-s+1) // 2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0) # 0번 인덱스에 있는 값 삭제

for x in a:
    print(x, end=' ')

# a, b = map(int, input().split())
# print(a, b)

# a, b = b, a
# print(a, b )