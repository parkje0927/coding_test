# 입출력
n = int(input())

data = list(map(int, input().split()))
data.sort(reverse=True)

data = list(map(int, input().split(" ")))
print(data)

n, m, k = map(int, input().split())
print(n, m, k)

import sys

data = sys.stdin.readline().rstrip()
print(data)

answer = 7
print(f"정답은 {answer} 입니다.")