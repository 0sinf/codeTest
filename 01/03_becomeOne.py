import time

start_time = time.time()

n, k = map(int, input().split())
#1 1.8
# cnt = 0
# while (n != 1):
#   if n % k == 0:
#     n //= k
#     cnt += 1
#     continue
#   n -= 1
#   cnt += 1
# print(cnt)

#2 1.6
ret = 0
while n >= k:
  while n % k != 0:
    n -= 1
    ret += 1
  n //= k
  ret += 1
while n > 1:
  n -= 1
  ret += 1
print(ret)

end_time = time.time()

print(end_time-start_time)
