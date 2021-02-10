import time

start_time = time.time()

# 맵크기 n,m
n, m = map(int, input().split())
# 현재 위치, 방향
a, b, d = map(int, input().split())

# 맵 정보 입력
mapInfo = []
for i in range(n):
  mapInfo.append(list(map(int, input().split())))

# 다녀간 공간인지 체크
mapKnown = [[0]*m for _ in range(n)]
mapKnown[a][b] = 1

#북 동 남 서 a는 북에서 떨어진 정도, b는 서에서 떨어진 정도
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

# 먼저 왼쪽 회전 시작 함수로 지정
def turn_left():
  global d #전역변수로 사용됨 (함수 지역변수 아님)
  d -= 1
  if d == -1:
    d = 3

# 시뮬레이션 시작
cnt = 1
turn_time = 0
while True:
    #왼쪽 회전
  turn_left()
  
  # 이동할 공간 확인
  na = a + da[d]
  nb = b + db[d]

  # 가본적 없고, 육지라면
  if mapKnown[na][nb] == 0 and mapInfo[na][nb] == 0:
    mapKnown[na][nb] = 1
    a = na
    b = nb
    cnt += 1
    turn_time = 0
    continue
  #가본적있거나 바다라면 다시 회전
  else:
    turn_time += 1

  # 회전을 4번해서 다시 본방향으로 왔다면
  if turn_time == 4:
    # 뒤로 갈 수 있는지 확인
    na = a - da[d]
    nb = b - db[d]
    if mapInfo[na][nb] == 0:
      a = na
      b = nb
    # 뒤로도 못가는 상황
    else:
      break
    turn_time = 0

print(cnt) 

end_time = time.time()

print(end_time-start_time)
