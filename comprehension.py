# 기존 방법
results = []
for i in [1,2,3,4,5,6,7,8,8,9,10]:
    result = i*i
    results.append(result)
print(results)

# comprehension 사용 = 표현식 내부에 for문 바로 기입
# (장점) 코드 효율 및 가독성 향상
results = [n*n for n in [1,2,3,4,5,6,7,8,8,9,10]]
print(results)

# 길이가 2 이하인 문자열 고르기
results = [s for s in ['a','as','ass','asss','assss'] if len(s) <= 2]
print(results)

# 1 - 100까지의 수 중 짝수 리스트 만들기
results = [i for i in range(1,101) if i%2==0]
print(results)

# list and set
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = [len(s) for s in strings]
print(lens)

lens = {len(s) for s in strings}
print(lens)

# dict (key - value 형태로 저장)
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
dicts = {s: len(s) for s in strings}
print(dicts)

# 1 - 100까지의 수 중 3 6 9
# 여기서 t = tuple
for t in [(i,'짝'*(str(i).count('3')+str(i).count('6')+str(i).count('9'))) for i in range(1,100) if '3' in str(i) or '6' in str(i) or '9' in str(i)]:
    print('%d : %s' % t)
































