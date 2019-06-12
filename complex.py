# 실수 + 허수의 형태 = 정확한 자료형 결정할 수 없음 = complex
a = 4+5j
print(a, type(a))

b = 7-2j
# 실수부 / 허수부 따로 연산 처리
print(a+b)

p = 2.5
q = 3
print(complex(p,q))




