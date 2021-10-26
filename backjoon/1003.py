# n = 0, 1, 2 일 때, 0과 1을 개수
d0 = [1, 0, 1]
d1 = [0, 1, 1]

def fibo(num):
  length = len(d0)
  if num >= length:
    # n = 3 부터 num까지 
    # f(n) = f(n-1) + f(n-2)를 생각해
    for i in range(length, num + 1):
      d0.append(d0[i - 1] + d0[i - 2])
      d1.append(d1[i - 1] + d1[i - 2])
  print('{} {}'.format(d0[num], d1[num]))

t = int(input())
for _ in range(t):
  fibo(int(input()))