'''
# 체스판 다시 칠하기

## 문제 설명

주어진 N X M 크기 판에서 8 X 8 의 체스판으로 만드는데 색을 바꾸어야 하는 칸의 갯수를 구한다.

## 자료 구조
  - graph
    - 타입: 이중 리스트
    - 저장 데이터: N X M 리스트, 입력받는 판의 정보

  - N
    - 타입: 정수형
    - 저장 데이터: 입력 받는 판의 행의 갯수
  
  - M
    - 타입: 정수형
    - 저장 데이터: 입력받는 판의 열의 갯수

  - min
    - 타입: 정수형
    - 저장 데이터: 바꿔야할 칸의 최소값 저장

## 풀이과정

1. N X M 판의 정보를 입력 받는다.

2. 반복문을 이용해 N X M 을 8 X 8 만큼씩 확인한다.

3. 확인할 때, 바꿔야 할 칸의 갯수를 계산해 최소값을 갱신한다.

'''
minimum = int(1e9)

wGraph = [
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
] * 4

bGraph = [
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
] * 4

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

for i in range(n - 7):
  for j in range(m - 7):
    
    cnt1 = 0
    cnt2 = 0
    for a in range(8):
      for b in range(8):
        if wGraph[a][b] != graph[i+a][j+b]:
          cnt1 += 1
        if bGraph[a][b] != graph[i+a][j+b]:
          cnt2 += 1
    
    minimum = min(min(cnt1, cnt2), minimum)

print(minimum)