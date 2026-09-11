# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # float 나눗셈
print(a // b)  # 몫
print(a % b)  # 나머지
print(a**b)  # 거듭제곱.

# 복합 대입 연산자
a = 0
a += 4
print(a)

a -= 2
print(a)

# 증감 연산자
# b = a++ 안됨
a += 1

# 비교 연산자
print(3 == 3.0)
print(3 != 4)
print("apple" > "banana")  # False
print(1 < 2 < 3)  # 1 < 2 and 2 < 3

# 논리 연산자 (and, or, not)
a = True
b = False
print(a and b)  # False
print(a or b)  # True
print(not a)  # False

# short-circuit 테스트
a = 10
b = 0

# print(a / b) division by zero
if a > 0 or a / b > 0:  # a > 0이 True이므로, a / b는 실행되지 않음
    print("Yes")
else:
    print("No")
