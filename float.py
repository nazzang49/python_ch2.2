a = 1.2

print(a, type(a))
print(isinstance(a,float))

b = 2.0
# 클래스 타입 대신 정수 범위인지 아닌지만 판별
print(b.is_integer())

b = 3e3
c = -0.2e-4
print(b,c)