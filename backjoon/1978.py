n = int(input())
lst = list(map(int, input().split()))

def isPrime(a):
  if a == 0 or a == 1:
    return False
  for i in range(2, int(a ** 0.5 + 1)):
    if a % i == 0:
      return False
  return True

cnt = 0
for i in lst:
  if isPrime(i):
    cnt += 1

print(cnt)