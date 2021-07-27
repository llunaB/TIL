

# Built-in Functions, Methods

### sorted() vs. .sort()

![image-20210727202701856](C:\Users\euiji\AppData\Roaming\Typora\typora-user-images\image-20210727202701856.png)

![image-20210727202728635](C:\Users\euiji\AppData\Roaming\Typora\typora-user-images\image-20210727202728635.png)

| `sorted`(*iterable*, ***, *key=None*, *reverse=False*)       | `sort`(***, *key=None*, *reverse=False*)                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| built-in function / 내장함수                                 | method / 메소드                                              |
| <u>**Return a new sorted list from the items in *iterable*.**</u> 새로운 리스트를 반환 | <u>***it does not return the sorted sequence.***</u> 새 리스트(복사본) 없고 None을 반환 |
| <u>***explicitly request a new sorted list instance***</u> 새 리스트를 만들고 원본은 유지 | ***<u>It modifies the list in-place</u>*** (and returns `None` to avoid confusion). 원본 데이터를 변경 |
| 원본데이터가 필요할 때 사용                                  | 원본데이터가 필요 없을 때 사용                               |
| the [`sorted()`]function accepts any iterable. / 모든 순회가능한 요소에 사용가능 (딕셔너리 등) | [`list.sort()`]method is only defined for lists / 리스트만 사용가능 |

```python
numbers = [3, 2, 5, 1]
result = sorted(numbers) # 원본 변경 없음
print(numbers, result)
# [3, 2, 5, 1] [1, 2, 3, 5]

numbers = [3, 2, 5, 1]
result = numbers.sort() # 원본 변경
print(numbers, result)
# [1, 2, 3, 5] None
```



### .extend() vs. .append()

![image-20210727213343199](C:\Users\euiji\AppData\Roaming\Typora\typora-user-images\image-20210727213343199.png)

![image-20210727213422585](C:\Users\euiji\AppData\Roaming\Typora\typora-user-images\image-20210727213422585.png)

- `append` adds an element to a list, and `extend` concatenates the first list with another list(or another iterable, not necessarily a list.)

| s.extend(t)` or `s += t                                      | s.append(x)                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| extends *s* with the contents of *t* (for the most part the same as `s[len(s):len(s)] = t`) | appends *x* to the end of the sequence (same as `s[len(s):len(s)] = [x]`) |
| 여러개 요소 가능                                             | list.append() takes exactly one argument (2 given) / 1개의 요소만 가능 |
| [str]                                                        | str                                                          |

```python
word = ['apple', 'banana', 'grape']
result = word.extend(['mango'])
print(word, result)
# ['apple', 'banana', 'grape', 'mango'] None

word = ['apple', 'banana', 'grape']
result = word.append(['mango'])
print(word, result)
# ['apple', 'banana', 'grape', ['mango']] None

word = ['apple', 'banana', 'grape']
result = word.extend(['mango', 'pear'])
print(word, result)
# ['apple', 'banana', 'grape', 'mango', 'pear'] None

word = ['apple', 'banana', 'grape']
result = word.append(['mango', 'pear'])
print(word, result)
# ['apple', 'banana', 'grape', ['mango', 'pear']] None
```

