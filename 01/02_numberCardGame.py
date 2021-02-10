import time

start_time = time.time()

n, m = map(int, input().split())

#1 9.3
# mat = []
# for i in range(n):
#   mat.append(list(map(int, input().split())))
# min_list = []
# for i in mat:
#   i.sort()
#   min_list.append(i[0])
# min_list.sort
# ret = min_list[n-1]
# print(ret)

#2
# ret = 0 12.7
# for i in range(n):
#   data = list(map(int, input().split()))
#   min_value = min(data)
#   ret = max (ret, min_value)
# print(ret)

#3 7.8
mat = []
for i in range(n):
  mat.append(list(map(int, input().split())))
ret = 0
for i in mat:
  i.sort()
  ret = max(ret, i[0])
print(ret)

end_time = time.time()

print(end_time-start_time)
