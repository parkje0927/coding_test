
# 기타 연산자
score = 85

if score >= 90:
    pass
else:
    print("성적이 90점 미만입니다.")

result = "Success" if score >= 80 else "Fail"
print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]
result = [i for i in a if i not in remove_set]
print(result)