# FAQs

### Why did changing list ‘y’ also change list ‘x’?

- Variables are simply names that refer to objects.
- Doing `y = x` does not create a copy of the list, but creates a new variable ` y` that refers to the same object `x` refers to.
- **This means that there is only one object, and both `x` and `y` refer to it.**

```python
# case - mutable

x = []	# lists are mutable
y = x
y.append(10)

print(x ,id(x)) # => [10] 1786298880768
print(y, id(y)) # => [10] 1786298880768
```

![image-20210727222825064](C:\Users\euiji\AppData\Roaming\Typora\typora-user-images\image-20210727222825064.png)

- However, **when integers are immutable**, we are not muting the int `5` by incrementing its value;
- Instead, we create a new object and assigning it to `x`.
- That is, changing which object `x` refers to.
- After this assignment, **we have two objects and two variables that refer to them.**

```python
# case - immutable

x = 5	# ints are immutable
y = x
x = x + 1	# 5 can't be mutated, so we create a new object here

print(x ,id(x)) # => 6 1786292496848
print(y, id(y)) # => 5 1786292496816

```

![image-20210727223612326](C:\Users\euiji\AppData\Roaming\Typora\typora-user-images\image-20210727223612326.png)

