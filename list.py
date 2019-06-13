# 리스트 생성(자료형 혼재 가능)
l = [1,2,3,4,'python']

# indexing
print(l[-3],l[-2],l[-1])

# slicing
l2 = l[0:4]
print(l[1:3])
print(l[:])
print(l[2:])
# 원소 거꾸로 재배열
print(l[len(l)-1::-1])

# 연결
l3 = l+[5,6,7]
print(l3)

# 확인
print(5 in l3)

# 삭제
del l3[0]
print(l3)

# mutable한 시퀀스 (tuple은 불가능)
a = ['apple', 'banana', 10, 20]
a[2] = a[2]+20
print(a)

# slicing을 통한 치환
a = [1, 12, 123, 1234]
a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

# 삭제와 똑같은 기능
a[1:2]=[]
print(a)

a = [1, 12, 123, 1234]

# 중간 삽입
a[1:1]=['a']
print(a)

# 마지막 삽입
a[5:]=[12345]
print(a)

# 여러 데이터 삽입
a[2:2]=[-12, -1, 0]
print(a)

#
# 객체 함수
#

a = [1, 12, 123, 1234]

# 중간 삽입
a.insert(1,'a')
print(a)

# 마지막 삽입
a.append(12345)
print(a)

# 앞 삽입
a.insert(0,0)
print(a)

# 제거(인덱스가 아닌 값으로 제거)
a.remove(12)
print(a)

# 확장(+d와 같은 역할)
a.extend([-1,0,-2])
print(a)

# 스택으로 활용
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())

# 큐로 활용
q = [1,2]
q.append(3)
q.append(4)
q.append(5)
print(q)

# sort() : 내장된 기능
l3 = [1,5,2,3,40,9]
# 기본적으로 오름차순 정렬
l3.sort(key=int)
print(l3)
l4 = sorted(l3)
print(l4)

l3 = [1,15,32,34,240,9,66]
l4 = sorted(l3)





















