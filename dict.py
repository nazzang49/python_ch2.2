import random

d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d))

print(d['basketball'])

d['volleyball'] = 6
print(d)

print(len(d))
print('soccer' in d)
print('volleyball' not in d)

d = dict()   # empty dict
print(d)

# key - value 인자 형태로 지정
d = dict(one=1, two=2)  # keyword arguments
print(d)

d = dict([('one', 1), ('two', 2)])   # tuple list
print(d)

# 갯수에 맞게 차례대로 key - value 지정
keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)

# 사전의 key
d = {}
print(d)

d[True] = 'true'
d[10] = '10'
d["twenty"] = '20'
# tuple 대신 list는 불가(mutable 하므로, key 값이 변경될 수 있음)
# key 값은 변경 불가
d[(1, 2, 3)] = '6'

print(d)

# key 객체 추출
keys = d.keys()
print(keys)
print(type(keys))

for key in keys:
    print('{0}:{1}'.format(key, d[key]))

# value 객체 추출
values = d.values()
print(values)
print(type(values))

# key - value 객체 함께 추출
items = d.items()
print(items)

# test
phone = {
    '둘리':'000-0000-0000',
    '마이콜':'000-0000-1111',
    '또치':'000-0000-2222'
}

n = phone.get('둘리')
print(n)

n = phone.get('길동')
print(n)
# 에러
# n = phone['길동']

# 길동 없으면 value 호출
n = phone.get('길동', '000-0000-0000')
print(n)
print(phone)

# 길동 없으면 value 호출 및 데이터 저장
n = phone.setdefault('길동', '000-0000-0000')
print(n)
print(phone)

n = phone.pop('둘리')
print(n)
print(phone)

n = phone.popitem()
print(n, type(n))
print(phone)

phone.update({'둘리': '010-1111-1111', '길동': '010-5555-5555'})
print(phone)

phone.clear()
print(phone)

d = {'c': 3, 'a': 1, 'b': 2}
for key in d:
    print(key, end=' ')
print()
for key in d:
    print(str(key) + ":" + str(d[key]), end=' ')
print()
for key in d:
    print("{0}:{1}".format(key, d[key]), end=' ')
print()
for key in d.keys():
    print("{0}:{1}".format(key, d[key]), end=' ')
print()
for key, value in d.items():
    print("{0}:{1}".format(key, value), end=' ')


min,max = 1, 100

while True:
    # 정답이 될 숫자
    n = random.randrange(max)+min
