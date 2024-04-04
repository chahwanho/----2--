#정수형 예제
a = 1234 
print(a)

a = -1234
print(a)

a= 0
print(a)

""" alt shift a = 주석"""

 #실수형
"""
a = 123.4
print(a)
a = -123.4
print(a)
a = 123.
print(a)
a = .123
print(a)
a = - .123
print(a)
 """
 # 지수 표기법
"""
a = 1e9
print(a)
a = 123e4
print(a)
a = 123e3
print(a)
a = 1.234e3
print(a)
a = 1234e-3 #1/1000
print(a) """

""" # 실수 표현 오류 예제
print (0.3+0.6) # 0.899999999999999
# 0.1+0.2 ==> 0.30000000000000004
# 0.2+0.4 ==> 0.600000000000001

if (0.3+0.6 == 0.9):
  print(True)
else:
  print(False)

if (round(0.3+0.6,4)==0.9):
  print(True)
else:
  print(False)

if ((0.3*10+0.6*10)/10 ==0.9):
  print(True)
else:
  print(False) """

# 에러 보정하는 라이브러리
# decimal 라이브러리 (모듈)
  
# 숫자형 연산자 연습
""" a = 1+2
b = 1-2
c = 1*2
d = 1/2 # 실수형
e = 1//2
f = 1%2
g = 1**2
print(a,b,c,d,e,f,g) """

a = '나는\t자연인이다.\n.\b'

print(a)

# % formatting
name = '이영진'
age = 53
testStr = '내 이름은 %s 이고, 내 나이는 %s이다.' %(name,age)
print(testStr)

name = '이영진'
age = 53
testStr = '내 이름은 {1} 이고, 내 나이는 {0}이다.' .format(age,name)
print(testStr)

 # raw string
print (r'안녕하세요\n @\b')