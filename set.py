# set 집합 생성

s = {1, 2, 3}
print(s, type(s))

s.add(4)
s.add(1)
s.discard(2)
s.remove(3)
s.update({2, 3})
s.clear()

# set 은 원소의 중복 제거
nums = [1,1,1,1,1,2,2,2,2,2,2]
s = set(nums)
print(s)

nums = list(s)
print(nums)

# 없는 원소 삭제 시 예외 발생 O
s.remove(2)
print(s)

# 없는 원소 삭제 시 예외 발생 X
s.discard(3)
print(s)

s.update({2,7,8})
print(s)


#
# 수학 집합 관련 객체 함수
#
s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {10,20,30}

# 합집합
s3 = s1.union(s2)
print(s3)

# 교집합
s3 = s1.intersection(s2)
print(s3)

# 차집합
s3 = s1.difference(s2)
print(s3)

# 합집합 - 교집합
s3 = s1.symmetric_difference(s2)
print(s3)

# print(s1.issuperset(s4))
# print(s5.issuperset(s1))
# print(s2.issubset(s3))




















