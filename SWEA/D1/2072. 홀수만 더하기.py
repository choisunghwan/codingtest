T = int(input())

for testcount in range(T) :
    nums = map(int,input().split())

    res = sum(n for n in nums if n%2==1)
    print( f"#{testcount+1} {res}" )