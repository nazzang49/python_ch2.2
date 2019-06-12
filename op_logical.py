# 비트 연산

a = 20
b = 30

print(not a<b)
print(a<b and a!=b)

print(~5)
print(~-1)

a = 3
print(a << 2)

a = 4
print(a >> 1)

# 캐스팅(0이 아닌 값은 모두 true로 인식)
print(bool(10), bool(0))

# << 연산자
a = 3
print(a << 2)

# >> 연산자
a = 4
print(a >> 1)
a = -4
print(a >> 1)

# bit and
a = 3
print(a & 2)
print(a | 8)
print(0x0f ^ 0x06)














