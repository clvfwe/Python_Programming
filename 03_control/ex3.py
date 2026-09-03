# for문

# for x in iterable객체:

for i in range(5):  # 0부터 4까지
    print(i, end=" ")

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10 2칸씩
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# 5 4 3 2 1 꺼꾸로
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
    i += 1
else:
    print(f"sum = {tot}")

print(sum(range(1, 11)))

s = "hi12!@한글鞠到延"

for c in s:
    print(c, end=" ")  # 파이썬은 문자 하나당 하나로. C는 한글 3
print()

# 구구단 출력
for i in range(2, 10):
    for j in range(2, 10):
        print(f"{i} * {j} = {i*j}", end=" ")
    print()
