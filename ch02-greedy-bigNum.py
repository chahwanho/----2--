n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # 오름차순

first = data[n-1]
second = data[n-2]

result = 0

"""while True:
 for i in range(k):
    if (m==0):
      break
    result+=first
    m-=1

  if(m==0): break
  result+=second
  m-=1"""
#count = int(m/(k+1)) * k #파이썬 나눗셈 결과 실수 결과
count = m//(k+1) * k
count += m % (k+1)

result += count * first
result += (m-count) * second


print(result)
