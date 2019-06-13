# unpacking error (갯수가 많지 않음)
# a, b = (10, 20, 30, 40)

# 갯수가 많지 않아도 가능한 경우 = 낱 원소 + 나머지는 리스트 처리
t = (1, 2, 3, 4, 5, 6)
a, *b = t
print(a,  b)

*a, b = t
print(a, b)

a, b, *c = t
print(a, b, c)

a, *b, c = t
print(a, b, c)

# 오버라이드 개념이 따로 존재하지 않음 (하나의 함수로 해결)
def sum(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

print(sum(1,2))
print(sum(1,2,3,4,5))
print(sum(1,2,3,4,5,6,7))

# c의 printf 함수 구현하기
# 방법 1
def printf(str,name,age):
    print(str%(name,age))

# 방법 2
# def printf(str,*tuple):
#     print(str%tuple)


printf('name:%s, age:%d','둘리',10)