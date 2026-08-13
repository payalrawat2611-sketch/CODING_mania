# Python Lists

A list stores multiple values in a single variable.

```python
numbers = [10, 20, 30, 40]
names = ["Payal", "Aman", "Riya"]

Access Elements

Indexing starts from 0.

numbers = [10, 20, 30, 40]

print(numbers[0])    # 10
print(numbers[-1])   # 40

Slicing
print(numbers[1:3])  # [20, 30]
Modify Elements

Lists are mutable, so elements can be changed.

numbers[0] = 100
print(numbers)
Useful Methods
numbers.append(50)      # Add at end
numbers.insert(1, 15)   # Add at index
numbers.remove(30)      # Remove value
numbers.pop()           # Remove last element
numbers.sort()          # Sort list
numbers.reverse()       # Reverse list
Length
print(len(numbers))
Keep in mind
Lists are written using [].
Lists are ordered and mutable.
Index starts from 0.
append() adds an element at the end.
remove() removes a specific value.
pop() removes an element using its index or the last element.