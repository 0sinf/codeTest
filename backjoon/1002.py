t = int(input())
for i in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  r = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

  # 두 점이 같은 위치인 경우
  if r == 0:
    if r1 == r2:
      print(-1)
    else:
      print(0)
  # 두 점이 다른 위치일 때
  else:
    if r1 + r2 == r or abs(r1 - r2) == r:
      print(1)
    elif r1 + r2 > r and abs(r1 - r2) < r:
      print(2)
    else:
      print(0)