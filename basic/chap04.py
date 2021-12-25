# 함수

def add(a, b):
    return a + b

print(add(3, 5))

def add(a, b):
    print("a + b = ", a + b)
add(b = 3, a = 5)

a = 0
def func():
    global a
    a += 1
for i in range(10):
    func()

print("a = ", a)

print((lambda a, b: a + b)(3, 7))
print((lambda a, b : a + b)(4, 5))