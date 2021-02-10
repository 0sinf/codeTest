import time

start_time = time.time()

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[N-1]
second = data[N-2]

#1 7.5
# ret = 0
# cnt = 0
# for i in range(M):
#   if not cnt == K-1:
#     ret += first
#     cnt += 1
#   else:
#     ret += second
#     cnt = 0

# print(ret)

#2 9.3
# sum_e = (first * K) + second
# ret = (M//(K+1) * sum_e) + (M%(K+1) * first)
# print(ret)

#3 7.1
cnt = int(M/(K+1)) * K
cnt += M % (K+1)

ret = 0
ret += cnt*first
ret += (M - cnt) * second
print(ret)

end_time = time.time()

print(end_time-start_time)
