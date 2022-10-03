def my_change(cost, paid):
    if cost > paid: #가격이 지불한값보다 크다면 
        print('paid has to be greater than or equal cost') # 더 지불해라 적어도 동등한 가격에 맞춰라
    else:
        denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
        change = []  # 보관
        remaining = paid-cost #거스름돈


        while remaining >= 0.01: #받아야될 거스름돈이 0.01 보다 크거나 같다면 반복
            for i in denominations: # i 에서 
                if i <= remaining:
                    change.append(i)
                    remaining -= i
                    break
    return change
    
my_change(27.57, 100)