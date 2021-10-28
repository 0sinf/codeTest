from itertools import combinations

lst = [int(input()) for _ in range(9)]

candis = list(combinations(lst, 7))

for candi in candis:
  if sum(candi) == 100:
    for i in sorted(list(candi)):
      print(i)
    break