from re import I
import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D1\\input.txt",'rt')



n = input() # 자연수 n 을 받는다. 하지만 int형으로 받지 않는다 왜냐하면 위에서 int형으로 받게 되면
# for 문에 len()함수를 적용시킬때 각 자릿수 개수 가 아닌 n 자연수 자체를 반복하기 때문이다.
result = 0
for i in range(len(n)):
    result += int(n[i]) # 자릿수 개수를 반복이 됨을 확인후 int형으로 형변환 시켜서 각 자릿수를 더해준다. int로 형변환 하지않으면 string 값으로 값을 더할 수 없다.
    
print(result)