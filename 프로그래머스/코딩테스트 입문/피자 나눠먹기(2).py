# a = 10
# b = 12

# 최대 공약수 구하기
# for i in range(min(a,b),0,-1):
#     if a % i == 0 and b % i == 0:
#         print(i) # 2
#         break


# 최소 공배수 구하기
# for i in range(max(a,b),(a*b)+1):
#     if i % a == 0 and i % b == 0:
#         print(i) # 60
#         break 



def solution(n):
    for i in range (max(n,6),(n*6)+1):
        if i % n == 0 and i % 6 == 0 :
            # print(i)
            break
    return i // 6

list =[6, 10, 4]
for a in list:
    print(solution(a))