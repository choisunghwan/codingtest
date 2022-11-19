import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # print(test_case)
    tc = int(input())
    score = list(map(int, input().split()))
    # print(test_case)
    # print(tc)
    # print(score)
    data = [0]*1001

    for i in score:
        data[i] += 1 # data배열의 i 번째에 1을 추가한다!
        # print(i)
    max_value = max(data)
    result = []
    for j in range(len(data)):
        if data[j] == max_value:
            result.append(j)
    print("#{} {}".format(test_case,max(result)))