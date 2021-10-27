def prime_numbers(n):
  check = [True] * n
  for i in range(2, int(n ** 0.5) + 1):
    if check[i]:
      for j in range(i + i, n, i):
        check[j] = False
  return ([i for i in range(2, n) if check[i]], check)

prime = prime_numbers(1000000)
lst = prime[0]
boolean_list = prime[1]

while True:
  n = int(input())
  if n == 0:
    break

  left = 0
  isCan = False
  while left < n // 2:
    if boolean_list[n - lst[left]]:
      isCan = True
      print('{} = {} + {}'.format(n, lst[left], n - lst[left]))
      break
    left += 1
  if not isCan:
    print("Goldbach's conjecture is wrong.")


# 시간초과

# def isPrime(num):
#   if num == 0 or num == 1:
#     return False
#   for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#       return False
#   return True

# def printResult(lst, n):
#   left = 0
#   right = len(lst) - 1
#   while left < right:
#     if lst[left] + lst[right] == n:
#       print('{} = {} + {}'.format(n, lst[left], lst[right]))
#       break
#     elif lst[left] + lst[right] < n:
#       left += 1
#     elif lst[left] + lst[right] > n:
#       right -= 1

# while True:
#   n = int(input())
#   if n == 0:
#     break
#   lst = [i for i in range(3, n) if isPrime(i)]
#   printResult(lst, n)

