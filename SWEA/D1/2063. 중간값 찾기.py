n = int(input()) 
nums = list(map(int,input().split()))
nums.sort()

mid = n //2
print(nums[mid])
#중간값을 찾기 -> 
# n값의 절반으로 나눈 값을 구한후-> 
# 그 값의 위치를 반환시키면 됨.
