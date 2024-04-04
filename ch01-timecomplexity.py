from random import randint # from 라이브러리명 import 구체적인 함수/클래스
import time # import 라이브러리명

arr = []
for _ in range(10000):
  arr.append(randint(1,100)) # 1~100의 임의의 정수를 추가

#print(arr)
"""start_time = time.time()

for i in range(len(arr)):
  min_index = i
  for j in range(i+1,len(arr)):
    if(arr[min_index]>arr[j]):
      min_index=j
  arr[i],arr[min_index] = arr[min_index],arr[i] # 스와프

end_time = time.time()

print('선택정렬 실행시간', end_time-start_time,"초 수행")"""

start_time = time.time()

arr.sort()

end_time = time.time()

print('정렬 실행시간', end_time-start_time,"초 수행")