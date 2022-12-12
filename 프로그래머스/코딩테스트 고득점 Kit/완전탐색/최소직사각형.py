def solution(sizes):
    answer = 0
    wallet = []
    for i in range(len(sizes)):
        sizes[i].sort()
        maximum = 0
    for i in range(2):
        for j in range(len(sizes)):
            if maximum <sizes[j][i]:
                maximum = sizes[j][i]
        wallet.append(maximum)
    answer=wallet[0]*wallet[1]
    return answer