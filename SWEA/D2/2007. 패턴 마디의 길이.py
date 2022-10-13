import sys
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\SWEA\\D2\\input.txt", 'rt')

t = int(input()) #testcase 입력.

for t in range(1, t+1):
    sentence = input()
    result = 0

    for i in range(1, 30):
        if sentence[i] == sentence[0]:
            if sentence[:i] == sentence[i:i*2]:
                result = i
                break
        if i == 29:
            result = 30
    print("#%d %d" %(t, result))

