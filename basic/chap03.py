# 반복문
# while

i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

# for
result = 0
for i in range(1, 10):
    result += i
print(result)

result = 0
scores = [90, 85, 77, 65, 97]
for i in range(len(scores)):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

cheating_list = {2, 4}
for i in range(len(scores)):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)