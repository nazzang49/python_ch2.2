# 튜플 생성

# 공튜플(최소 1개 이상의 원소가 존재할 때 튜플 성립)
t = ()
# 원소가 1개이면 콤마 표기
t = (1,)
t = (1,2,3)

print(t)

#
# sequence 지원 연산
#

# indexing
print(t[-2], t[-1], t[0], t[1], t[2])
# 1 ~ 2번째자리 원소까지
print(t[1:3])
print(t[:])

# for문 없이 반복
print(t * 2)
# 추가
print(t + (3, 4, 5))
# 길이
print(len(t))
# 원소 존재 여부
print(5 in t)

# tuple은 immutable 한 시퀀스(원소 변경 불가 -> 아래 구문 예외 발생)
t = ('apple', 'banana', 10, 20)
# t[2] = t[2] + 90

# auto packing (자동으로 tuple 변환)
t = 10, 20, 30, 'python'
print(t)
print(type(t))

# unpacking tuple
a, b, c, d = t
print(a, b, c, d)

# unpacking list
a, b, c, d = [10, 20, 30, 'python']
print(a, b, c, d)


#
# 객체 함수
#

t = (20,30,10,20)
# 첫 등장 위치
print(t.index(20))
# 갯수
print(t.count(20))

# 변환
t = (1,2,3,3)

# tuple -> set (중복 자동 제외)
s = set(t)

# tuple -> list
l = list(t)

# 배열 종류 간 형변환 모두 가능
print(s)
print(t)
print(l)

















