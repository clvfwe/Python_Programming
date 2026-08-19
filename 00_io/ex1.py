# 입출력 처리

# 정수 1개 입력
a = input()
print(a)
print(type(a))

# 정수 변환
a = input()
a = int(a)
print(type(a))

a = int(input())
print(type(a))

# 실수 입력
b = float(input())
print(b, type(b))

# 정수 2개 입력
# 100
# 200 입력
a = int(input())
b = int(input())
print(a, b)

# 100 200 입력
a, b = map(int, input().split())
print(a, b)
# split() : 공백 기준으로 문자열을 나눠서 리스트로 반환
# map(함수, 리스트) : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 리스트로 변환
a = list(map(int, input().split()))
print(a)
