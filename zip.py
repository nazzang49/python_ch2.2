# 여러개 튜플 or 리스트 or 셋을 서로 조합

# set1
seq1 = {'foo', 'bar', 'baz'}
# set2
seq2 = {'one', 'two', 'three'}
z = zip(seq1, seq2)
print(z)
print(type(z))

# set 객체는 순서가 없으므로 실행할 때 마다 랜덤 매칭
for t in z:
    print(t, type(t))

# 아래와 같이 unzip 가능
# seq1, seq2 = zip(*a)