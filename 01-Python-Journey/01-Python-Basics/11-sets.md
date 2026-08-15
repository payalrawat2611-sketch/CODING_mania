# Python Sets


A set is an unordered collection of unique values. Sets are written using `{}` and automatically remove duplicate values.


```python
numbers = {10, 20, 30, 20}
print(numbers)  # {10, 20, 30}

Use add() to add elements and remove() or discard() to remove them.

numbers.add(40)
numbers.remove(20)

Sets support operations like union |, intersection &, and difference -.

a = {1, 2, 3}
b = {3, 4, 5}


print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
Keep in mind
Sets contain only unique values.
Sets are unordered and do not support indexing.
Useful for removing duplicates and performing set operations.