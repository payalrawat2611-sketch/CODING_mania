# Python Tuples

A tuple stores multiple values in a single variable.

```python
numbers = (10, 20, 30, 40)

Access Elements

Indexing starts from 0.

Slicing
print(numbers[1:3])  # (20, 30)
Tuple is Immutable

Tuple elements cannot be changed after creation.

numbers = (10, 20, 30)


# numbers[0] = 100  # Error
Useful Methods
numbers = (10, 20, 20, 30)


print(numbers.count(20))  # 2
print(numbers.index(30))  # 3
Length
print(len(numbers))
Keep in mind
Tuples are written using ().
Tuples are ordered and immutable.
Indexing starts from 0.
Use a tuple when the data should not be changed.
Tuples generally have fewer methods than lists.
