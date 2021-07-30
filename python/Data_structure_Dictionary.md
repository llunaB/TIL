# 데이터 구조

## 딕셔너리 Dictionary

### <u>Create</u>

```python
my_dict = {}
my_dict['apple'] = '사과'

print(my_dict) # => {'apple': '사과'}
```



### <u>Read</u>

##### .get(key[, default])

- key를 통해 value를 가져옵니다.
- 절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.get('apple') # => '사과'
my_dict.get('pineapple', 0) #=> 0  key가 없다면 0을 반환
```



### <u>Update</u>

##### .update()

- 값을 제공하는 key, value로 덮어씁니다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple='apppple')

print(my_dict) 
# => {'apple': 'apppple', 'banana': '바나나', 'melon': '멜론'}
```



### <u>Delete</u>

##### .pop(key[, default])

- key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.
- default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.pop('apple')

print(my_dict) # => {'banana': '바나나'}

my_dict.pop('melon') # -> KeyError: 'melon'
```



### dictionary 

- can be created by placing a comma-separated list of `key:value` pairs within braces.

