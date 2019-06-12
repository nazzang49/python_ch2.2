# 관계 연산

print(1 > 0)
print(1 != 0)
print(1 == 0)

# 복합 관계 연산 가능
a = 6
print(0 < a < 10)
print(0 < a and a < 10)

# 수치형 외 관계 연산 가능
# 사전 순
print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] > [1, 2, 0])

# tuple
c = (1,2,4)
# list (가변 배열)
d = [1,3,2]
print(c, type(c))
print(d, type(d))

# append로 배열에 추가
d.append(1)
print(d, type(d))