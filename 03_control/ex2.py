# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 1
while i < 11:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("End")  # break로 끝나면 else문은 실행되지 않음

# while else문 예제
nums = [1, 3, 5, 7, 9]
target = 2
i = 0
while i <= len(nums):
    if [i] == target:
        print(f"{target} found.")
        break
    i += 1
else:
    print(f"{target} not found.")

# 1 ~ 10까지의 합
i = 1
tot = 0
while i < 11:
    tot += i
    i += 1
print(f"sum: {tot}")

# 1 ~ 10까지 짝수 합
i = 1
tot = 0
while i < 11:
    if i % 2 == 0:
        tot += i
    i += 1
#   if i % 2 == 1:
#       i += 1
#       continue
print(f"sum: {tot}")
