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