def solution(array, n):
    n_count = 0
    for i in  array:
        # print(i)
        if (i == n):
            n_count += 1
    # print(n_count)
    return n_count

# 예제 사용
print(solution([1, 1, 2, 3, 4, 5], 1))  # 결과: 2
print(solution([0, 2, 3, 4], 1))  # 결과: 0
