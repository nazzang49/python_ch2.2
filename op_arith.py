# 산술 연산

print(2+3)
print(2-3)
print(2*3)
print(2%3)

# 나눗셈의 경우 실수형으로 결과 반환(아래 세가지 결과 같음)
print(2/3)
print(2.0/3)
print(2.0/3.0)

# //(몫 연산) = 자바에서와 같이 결과 int 처리
print(2//3)
# **(지수승)
print(2**3)

# 몫과 나머지 두개의 결과 동시 반환
result, last = divmod(2, 3)
print(result, last)

# 하나의 변수로 받으면 tuple 클래스(immutable = 변경 불가) 타입
t = divmod(2, 3)
print(t, type(t))

# 결합순서 주의(아래 두가지 결과 같음)
# 2의 81승이 됨
print(2**3**4)
print(2**(3**4))



