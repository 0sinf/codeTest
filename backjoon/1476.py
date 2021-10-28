'''
1. 문제 정의
  수 3개를 이용해 연도를 나타낸다.
  지구를 나타내는 수 1 <= E <= 15
  태양을 나타내는 수 1 <= S <= 28
  달을 나타내는 수 1 <= M <= 19

  1년이 지날 때마다 세수 모두 1씩 증가
  범위를 넘어가면 다시 1부터.

  입력된 연도가 우리가 알고 있는 연도로 몇 년인지 구하기.

2. 풀이 방식
  1 1 1 에서 얼마나 갔는지 해본다.
'''

E, S, M = map(int, input().split())

now = 1
e, s, m = 1, 1, 1
while True:
  if e == E and s == S and m == M:
    break

  e += 1
  s += 1
  m += 1
  now += 1
  
  if e == 16:
    e = 1
  if s == 29:
    s = 1
  if m == 20:
    m = 1

print(now)