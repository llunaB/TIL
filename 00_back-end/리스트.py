## 메서드

fruits = ['apple', 'banana', 'orange']
del fruits[1]
print(fruits)

# 데이터 추가
fruits.append('apple')
fruits.append(['apple','banana'])

# 데이터 삭제
fruits.pop() # 인덱스 추가 가능
fruits.remove('apple')

#인덱스 구하기
fruits.index('apple')

# 개수 구하기
fruits.count('banana')

# 정렬하기 
fruits.sort()

# enumerate!!
numbers = [5,2, 8, 1, 10]
for index, number in enumerate(numbers, 1): # 인덱스 시작번호 1로 지정
    print(f'{index}번째 글입니다. 숫자 : {number}')


