"""def add(a,b):
  # res = a+b
  # return res
  return a+b

result = add(5,3)
# a = 5, b = 3 실행한 후 함수 add의 실행문이 동작하게 됨
print(result)

def add(a,b):
  print('함수의 결과: ', a+b)
  #return None 생략되있음

res = add(6,7)
print(res)"""
"""
def add(a,b=3):
  print('함수의 결과: ', a+b)

add(b=5, a=1) #파라미터를 지정하여 호출 가능, 순서 상관없음
add(4) #파라미터의 default값 지정하여 실행가능"""
"""
a = 0

def func():
  #global a #함수 외부의 a 변수 사용 선언
  print(a) # 함수내에서 외부 변수 a의 변경사용이 없다면 읽기는 가능
  #a+=1

  for i in range(10): #0~9
    func()

print(a)"""

arr = [1,2,3,4]
def func():
  arr = [2,3,4]
  arr.append(5)
  print(arr)

func()
print(arr)

#packing

def operator(a,b):
  sum = a+b
  sub = a-b
  mul = a*b
  div = a/b #정수값이 아님, 실수
  return sum,sub,mul,div #packing

a,b,c,d = operator(3, 18) # unpacking
print(a,b,c,d)