n = 1260
count = 0

coin_type=[500,100,50,10]

for coin in coin_type:
  count += n // coin
  n %= coin
  """ 몫 = n // coin
  나머지 = n % coin
  count = count+몫
  n = 나머지"""

print(count)