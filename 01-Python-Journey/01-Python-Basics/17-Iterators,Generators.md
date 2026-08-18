## Python Iterators & Generators
1. What is an Iterator?

An iterator is an object that allows you to access elements one by one.

Python provides two important functions:

iter() → creates an iterator
next() → gets the next value
numbers = [10, 20, 30]


it = iter(numbers)


print(next(it))
print(next(it))
print(next(it))

Output:

10
20
30
2. for Loop and Iterators

A for loop internally uses an iterator to access elements one by one.

numbers = [10, 20, 30]


for num in numbers:
    print(num)

So you don't normally need to manually use iter() and next() with a for loop.

3. What is a Generator?

A generator is a special type of iterator that generates values one at a time instead of storing all values in memory.

Generators are created using the yield keyword.

def numbers():
    yield 1
    yield 2
    yield 3


for num in numbers():
    print(num)

Output:

1
2
3
4. yield vs return

return ends the function completely.

def test():
    return 10
    return 20

Only 10 is returned.

yield pauses the function and remembers its state.

def test():
    yield 10
    yield 20

Both values can be generated one by one.

5. Why Use Generators?

Generators are useful when working with large amounts of data because they don't store all values in memory at once.

Example:

def count(n):
    for i in range(1, n + 1):
        yield i


for x in count(5):
    print(x)

The values are generated one at a time.

🧠 Remember
Iterator → accesses elements one by one.
iter() → creates an iterator.
next() → gets the next value.
Generator → creates values one at a time.
yield → pauses and resumes a generator.
Generators are memory efficient.
for loops internally use iterators.