import time

start_time = time.time()

#1 1.9
# data = input()
# x = ord(data[0])
# y = int(data[1])

# xList = ['a','b','c','d','e','f','g','h']
# yList = [1,2,3,4,5,6,7,8]
# move_type = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

# cnt = 0
# for i, j in move_type:
#   nx = x + i
#   ny = y + j
#   if chr(nx) in xList and ny in yList:
#     cnt += 1
# print(cnt)

#2 2.2
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1
steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

res = 0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    res += 1
print(res)

end_time = time.time()

print(end_time-start_time)
