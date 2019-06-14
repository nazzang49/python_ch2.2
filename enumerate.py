# 기본 format 형식
i = 0
for value in ['red', 'yellow', 'blue', 'white', 'gray']:
    print('{0}: {1}'.format(i, value))
    i += 1

print()

# cf) enumerate 함수 사용 = 반복문에 자동으로 index 할당이 필요할 때 유용
for i, value in enumerate(['red', 'yellow', 'blue', 'white', 'gray']):
    print('{0}: {1}'.format(i, value))

