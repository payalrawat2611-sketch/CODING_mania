## enumerate()

enumerate() gives both the index and value while looping.

names = ["A", "B", "C"]


for index, name in enumerate(names):
    print(index, name)

Output:

0 A
1 B
2 C

You can also choose the starting index:

for index, name in enumerate(names, start=1):
    print(index, name)

Output:

1 A
2 B
3 C


## zip()

zip() combines elements from multiple iterables.

names = ["A", "B", "C"]
marks = [80, 90, 85]


for name, mark in zip(names, marks):
    print(name, mark)

Output:

A 80
B 90
C 85

It stops when the shortest iterable ends.

a = [1, 2, 3]
b = ["a", "b"]


print(list(zip(a, b)))

Output:

[(1, 'a'), (2, 'b')]
🧠 Remember
enumerate() → gives index + value
zip() → combines multiple iterables
enumerate(list, start=1) → changes starting index
zip() stops at the shortest iterable
Both are especially useful when solving DSA problems.