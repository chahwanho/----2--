n = int(input('동전의 갯수 입력: '))#동전 갯수
inData = list(map(int, input('동전 단위 입력: ').split()))#동전들의 단위

inData = sorted(inData)

target = 1
for i in inData:
  if (i>target):
    break
  else:
    target+=i

print(target)