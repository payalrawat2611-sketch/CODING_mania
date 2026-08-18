Lambda

A lambda is a small anonymous function written in one line.

square = lambda x: x * x


print(square(5))

Output:

25
Syntax
lambda arguments: expression
map()

map() applies a function to every element of an iterable.

numbers = [1, 2, 3, 4]


squares = list(map(lambda x: x * x, numbers))


print(squares)

Output:

[1, 4, 9, 16]
filter()

filter() keeps only the elements that satisfy a condition.

numbers = [1, 2, 3, 4, 5, 6]


even = list(filter(lambda x: x % 2 == 0, numbers))


print(even)

Output:

[2, 4, 6]
reduce()

reduce() repeatedly applies a function to combine all elements into one result.

It is available in the functools module.

from functools import reduce


numbers = [1, 2, 3, 4]


result = reduce(lambda a, b: a + b, numbers)


print(result)

Output:

10
🧠 Remember
lambda → Creates a small anonymous function.
map() → Transforms every element.
filter() → Selects elements based on a condition.
reduce() → Combines elements into one result.
reduce() requires from functools import reduce.