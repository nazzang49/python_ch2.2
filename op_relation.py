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

# tuple과 list는 서로 비교할 수  없음(캐스팅하면 가능)
# print((1, 3, 2) > [1, 2, 0])
print(list((1, 3, 2)) > [1, 2, 0])

# tuple
c = (1,2,4)
# list (가변 배열)
d = [1,3,2]
print(c, type(c))
print(d, type(d))

# append로 배열에 추가
d.append(1)
print(d, type(d))

# 동질성(값) 및 동일성(객체 주소) 비교
a = 10
b = 20
c = a
print(a == b) #f
print(a is b) #f
print(a is c) #t
print(a == c) #t
print(a is d) #f

# list는 동질성만 만족
# tuple은 동질성 / 동일성 모두 만족(변경 불가이기 때문에 동일한 객체로 취급)
l1 = [1,2,3]
l2 = [1,2,3]

print(l1 == l2) #t
print(l1 is l2) #f

l3 = (1,2,3)
l4 = (1,2,3)

print(l3 == l4) #t
print(l3 is l4) #t

# 논리의 계산 순서(명확한 것을 기준으로 출력)
print([] or 'logical') #logical
print('operator' or 'logical') #operator
print('' or 'logical')
# 출력 X (or 연산과 달리 앞쪽에서 false가 되면 전체가 false 되므로)
print('' and 'logical')
print('ok')
print(None and 1)

s = 'hello world'

# msg가 명확하면 = true = and 뒤쪽으로 이동 = print or 또 다른 비교 연산
def f(msg):
    msg and print(msg)

f(s)
f('park')

print(bool(10), bool(0))
print(bool(3.14), bool(0.))
print(bool('abc'), bool(''))
print(bool([1, 2, 3]), bool([]))
print(bool((1, 2, 3)), bool(()))
print(bool({1:2}), bool({}))
print(bool(None))



