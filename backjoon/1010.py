'''
# 다리놓기

## 문제 설명

강 서편 N개의 site, 강 동편 M개의 site를 잇는 N개의 다리가
서로 겹치지 않게 세워질 수 있는 경우의 수를 구하라.

## 자료 구조
  - t
    - 타입: 정수형
    - 저장 데이터: 테스트 케이스 갯수
  
  - n
    - 타입: 정수형
    - 저장 데이터: 왼편 site의 갯수
  
  - m
    - 타입: 정수형
    - 저장 데이터: 오른편 site의 갯수

  - candi
    - 타입: 리스트
    - 저장 데이터: 순열의 결과 값 출력

  - lst
    - 타입: 리스트
    - 저장 데이터: m개 사이트의 번호

## 풀이과정

1. 테스트 케이스의 갯수를 입력받고 그 숫자대로 반복문을 실행한다.

2. 반복문에서 n, m의 값을 입력받는다.

3. 조합을 사용해 mCn의 값을 찾는다.

'''

# from itertools import combinations

# t = int(input())
# for _ in range(t):
#   n, m = map(int, input().split())
#   lst = [ i for i in range(m) ]
#   candi = list(combinations(lst, n));
  
#   print(len(candi))

'''
메모리 초과로 인한 에러
'''

import math

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  result = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
  print(result)

'''
조합 모듈로 메모리 초과가 나와서
조합의 갯수를 계산하는 공식으로 해결하였음.

    m!
----------- = m C n
n! * (m-n)!
'''