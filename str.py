# 한 줄 문자열 정의
s = ''
print(s, type(s))

str1 = 'Hello World'
print(str1, type(str1))
print(isinstance(str1,str))

# 여러 줄 주석으로 활용 가능
str2 = '''ABC
1234
가나다라
'''
print(str2)

# escape
print("Hello\nWorld\nI say 'hello world'")

# 문자열 연산
str1 = 'First String'
str2 = 'Second String'
print(str1+str2)
print(str1[2])
print(str1[-1])
print(str1[-2])
print(len(str2))

# slicing
print(str2[2:5])

# len
# 여기서는 생략 가능
print(str2[2:len(str2)])

# 앞에서부터 인덱스 = 0 시작
# 뒤에서부터 인덱스 = -1 시작
s = 'Python'

# 인덱스 값이 마이너스이면 뒤에서부터 읽음
print(s[-1])

# 마지막 두개 문자
print(s[-2:])

# 마지막 두개 문자 제외한 나머지 문자
print(s[:-2])

# swap
print(s[::-1]) #nohtyP
print(s[1::-1]) #yP

# 마지막 두개 문자
print(s[:-3:-1])

# 연결(+)
print(str1+' '+str2)

# 문자열 객체 연결은 문자열끼리만 가능
# print('둘리'+10)

# 반복(for문 없이 곱셈 기호로 대체 가능)\
print(str1*3)

# 이중 for문 사용하지 않고 별 찍기
for i in range(1,11):
    # end=''는 공백없이 붙여 출력
    print('*'*i,end='')
    print()

# in / not in 연산(해당 문자열 내 존재 여부)
print('F' in str1)
print('S' not in str1)

# str 객체는 immutable
# 동일한 변수명으로 str -> list 변경 불가
# str1[0] = 'f'

name='또치'
age=28

# 서식 format
print('name : '+format(name, 's')+', age : '+format(age, 'd'))
f = 'name : %s,  age : %d'
print(f%(name, age))
print(f%('또치', 28))

f = 'name:%(n)s, age: %(a)d'
print(f%{'n':'또치', 'a':28})

# 객체 함수

# 대소문자
s = 'i like Python'
print(s.upper())
print(s.lower())
# 대 -> 소 / 소 -> 대
print(s.swapcase())
# 첫 문자만 대문자로
print(s.capitalize())
# 단어별 첫 문자를 대문자로
print(s.title())

# 검색
s = 'I Like Python, And Also I Like Java'
# Like가 처음으로 나오는 위치
print(s.count("Like"))
print(s.find("Like"))
# 5번째 인덱스 이후로 찾음
print(s.find("Like", 5))
print(s.find("JavaScript"))
# 오른쪽에서부터 찾음
print(s.rfind("Like"))
# index는 해당 문자열 없으면 exception / find는 해당 문자열 없으면 -1 반환
# find가 효율적
print(s.index("Like"))
# 있으면 true
print(s.startswith("I Like"))
print(s.endswith("Java"))

# 편집과 치환(strip = trim)
s = '      lunchtime is back   '
print('-------' + s.strip() + '-------')
print('-------' + s.rstrip() + '-------')
print('-------' + s.lstrip() + '-------')

s = '<abc>click<abc>'
print('-------' + s.strip('<>') + '-------')
print('-------' + s.strip('><') + '-------')

s = 'Hello Java'
print(s.replace('Java', 'Python'))

# 분리와 결합
s = 'spam and ham'
# split 하는 순간 리스트 배열 생성
l = s.split(' and ')
print(l, type(l))

s2 = ':'.join(l)
print(s2)

s3 = 'one:two:three:four:five'
print(s3.split(':'))
# 두개만 split하고 나머지는 하나의 문자열 그대로 추가
print(s3.split(':',2))

# 개행 자르기
lines = '''1st line
2nd line 
3rd line
4th line
'''
print(lines.split('\n'))
# 가장 마지막 빈 줄 처리
print(lines.splitlines())

# 판별(islower / isupper도 가능)
print('1234'.isdigit())
print('abcd'.isalpha())
print('    '.isspace())
print('\r\n'.isspace())
print('\t'.isspace())

# '0' 채우기
print('20'.zfill(5))

# 서식 : 객체 함수
print('name:{}, age:{}'.format('둘리',10))
print('name:{0}, age:{1}'.format('둘리',10))
print('name:{1}, age:{0}'.format(10,'둘리'))
print('{:3}의 제곱근은 {:.7}'.format(2,2**0.5))
print('name:{n}, age:{a}'.format_map(
    {'n':'둘리', 'a':10}
))







