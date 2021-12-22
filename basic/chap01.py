# 자료형
a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

a = 1e9
print(a)

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

a = 7
b = 3
print("a / b : ", a / b)
print("a % b : ", a % b)
print("a // b : ", a // b)
print("a ** b : ", a ** b)

# list

a = [1, 2, 3, 4, 5]
print(a)

a = list()
print(a)

a = [0]
a = a * 10
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])
print(a[-3])
a[3] = 100
print(a)

print(a[1:4])

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

def printList(a):
    print(a)

a = [7, 1, 3]
a.append(9)
printList(a)

a.sort()
printList(a)

a.sort(reverse=True)
printList(a)

a.insert(1, 5)
printList(a)

a.count(7)
printList(a)

a.remove(7)
printList(a)

a = [1, 2, 3, 4, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# 문자열

data = "Hello World"
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 튜플
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호([]) 를 이용하지만, 튜플은 소괄호(())를 이용한다.
# 다익스트라 최단 경로 알고리즘처럼 최단 경로를 찾아주는 알고리즘의 내부에서는 우선순위 큐를 이용하는데,
# 해당 알고리즘에서 우선순위 큐에 한 번 들어간 값은 변경되지 않는다.
# 흔히 다익스트라 최단 경로 알고리즘에서는 '비용' 과 '노드번호' 라는 서로 다른 성질의 데이터를
# (비용, 노드 번호) 의 형태로 함께 튜플로 묶어서 관리하는 것이 관례이다.

a = (1, 2, 3, 4)
print(a)

# a[2] = 7 -> error

# 사전 자료형
# 내부적으로 해시 테이블을 이용하므로 기본적으로 데이터의 검색 및 수정에 있어서 O(1) 의 시간에 처리할 수 있다.
# 키-값 쌍으로 구성된 데이터를 처리함에 있어서 리스트보다 훨씬 빠르게 동작한다.

data = dict()
data['a'] = 'Apple'
data['a'] = 'Apple2'
data['b'] = 'Banana'

print(data)

if 'a' in data:
    print('"a" 를 키로 가지는 데이터가 존재합니다.')

key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)

for key in key_list:
    print(data[key])

# 집합
# 집합 자료형은 기본적으로 리스트 혹은 문자열을 이용해서 만들 수 있는데, 중복을 허용하지 않고 순서가 없다.
# 리스트나 튜플 => 순서가 있기 때문에 인덱싱을 통해서 자료형 값을 얻을 수 있다.
# 사전 자료형과 집합 자료형 => 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
# O(1)

data = set()
data = {1, 2, 1, 2, 3, 4, 5}
print(data)

a = {1, 1, 2, 3, 4, 5}
b = set({3, 4, 5, 6, 7})
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

data = set([1, 2, 3, 4, 4])
data = set((1, 2, 3, 4, 4))
data = set({1, 2, 3})
data.add(4)
print(data)
data.add(4)
print(data)

data.update([5, 5])
print(data)

data.remove(3)
print(data)