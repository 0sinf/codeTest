from itertools import combinations

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

t = int(input())

for _ in range(t):
  total = 0
  lst = list(map(int, input().split()))[1:]
  for a, b in list(combinations(lst, 2)):
    if gcd(a, b) != 0:
      total += gcd(a, b)
  
  print(total)