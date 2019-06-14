# range = 범위 시퀀스
seq = range(10)
print(seq, type(seq))
# list로 변경 가능
print(list(seq))
print(seq[0:])
print(len(seq))

for i in seq:
    print(i)

seq2 = range(5, 15)
for i in seq2:
    print(i)

# 0 ~ -9까지 -1씩 감소하는 반복문
seq3 = range(0, -10, -1)
for i in seq3:
    print(i)
