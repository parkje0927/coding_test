# 내장 함수
result = sum([1, 2, 3, 4, 5])
print(result)

result = min(1, 5)
print(result)

result = max(7, 100, 3, 9)
print(result)

result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 4, 5], reverse=True)
print(result)

result = sorted([("a", 1), ("c", 5), ("b", 2)], key=lambda x : x[0])
print(result)

# itertools
from itertools import permutations, combinations, product, combinations_with_replacement

# 순열 : 중복 O
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 조합 : 순서 고려 X
result = list(combinations(data, 3))
print(result) # [('A', 'B', 'C')]
result = list(combinations(data, 2))
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 허용 O
# 2개를 뽑는 모든 순열 구하기(중복 허용)
result = list(product(data, repeat = 2))
print(result)

# 순서 고려하지 않고 2개 뽑기(중복 허용)
result = list(combinations_with_replacement(data, 2))
print(result)

# heapq
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
print(result)

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
print(result)

# bisect
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

# collections
from collections import deque, Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

counter = Counter(['red', 'red', 'blue'])
print(counter['blue'])
print(counter['red'])


