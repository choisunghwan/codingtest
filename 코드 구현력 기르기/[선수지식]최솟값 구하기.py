#최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # 가장 큰 값 초기화.(무한대 값)
#arrMin=arr[0] 으로 해도 된다. 왜냐하면 하나씩 비교하면서 최솟값을 구하면 되는거니까.


for i in range(len(arr)): #0부터 7까지 반복(총 8번) . 인덱스 번호로 생각해야함.
    if arr[i] < arrMin:
        arrMin=arr[i]
print(arrMin)