/*Regular Expressions (Regex) are used to search,  find, match, extract, validate, 
and replace patterns in text.*/

// Python provides Regular Expressions through the built-in 're' module.

# 1. Importing the re Module

import re


# 2. re.search()

// re.search() searches for a pattern anywhere in a string.

text = "I am learning Python"

result = re.search("Python", text)

print(result)


# We can check whether a pattern was found.

if re.search("Python", text):
    print("Python found")
else:
    print("Python not found")


# If the pattern does not exist, it returns None.

result = re.search("Java", text)

print(result)


# --------------------------------------------------
# 3. re.match()
# --------------------------------------------------

# re.match() checks for a pattern only
# at the beginning of a string.

text = "Python is powerful"

result = re.match("Python", text)

print(result)


# This will not match because "powerful"
# is not at the beginning.

result = re.match("powerful", text)

print(result)


# Difference:
#
# re.match()  -> checks from the beginning
# re.search() -> searches anywhere


# --------------------------------------------------
# 4. re.findall()
# --------------------------------------------------

# re.findall() returns all occurrences
# of a pattern.

text = "cat dog cat bird cat"

result = re.findall("cat", text)

print(result)

# Output:
# ['cat', 'cat', 'cat']


# If no match is found, an empty list is returned.

result = re.findall("fish", text)

print(result)

# Output:
# []


# --------------------------------------------------
# 5. re.sub()
# --------------------------------------------------

# re.sub() is used to replace matching text.

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)

# Output:
# I like Python


# --------------------------------------------------
# 6. re.split()
# --------------------------------------------------

# re.split() splits a string according to
# a regular expression pattern.

text = "apple,banana;orange"

result = re.split(r"[,;]", text)

print(result)

# Output:
# ['apple', 'banana', 'orange']


# --------------------------------------------------
# 7. Special Regex Characters
# --------------------------------------------------

# \d -> matches a digit

text = "My age is 20"

result = re.findall(r"\d", text)

print(result)

# Output:
# ['2', '0']


# \d+ -> matches one or more digits

text = "I have 20 apples and 15 oranges"

result = re.findall(r"\d+", text)

print(result)

# Output:
# ['20', '15']


# --------------------------------------------------
# 8. \w
# --------------------------------------------------

# \w matches word characters:
# letters, digits, and underscore.

text = "Python_123"

result = re.findall(r"\w", text)

print(result)


# --------------------------------------------------
# 9. \s
# --------------------------------------------------

# \s matches whitespace characters.

text = "Hello World"

result = re.findall(r"\s", text)

print(result)


# --------------------------------------------------
# 10. Character Sets []
# --------------------------------------------------

# Square brackets allow us to specify
# a group of characters.

text = "cat bat rat"

result = re.findall(r"[cbr]at", text)

print(result)

# Output:
# ['cat', 'bat', 'rat']


# --------------------------------------------------
# 11. [0-9]
# --------------------------------------------------

# [0-9] matches digits from 0 to 9.

text = "My numbers are 25 and 48"

result = re.findall(r"[0-9]+", text)

print(result)

# Output:
# ['25', '48']


# --------------------------------------------------
# 12. [a-z]
# --------------------------------------------------

# [a-z] matches lowercase letters.

text = "hello PYTHON"

result = re.findall(r"[a-z]+", text)

print(result)

# Output:
# ['hello']


# --------------------------------------------------
# 13. The + Quantifier
# --------------------------------------------------

# + means one or more occurrences.

text = "a aa aaa aaaa"

result = re.findall(r"a+", text)

print(result)

# Output:
# ['a', 'aa', 'aaa', 'aaaa']


# --------------------------------------------------
# 14. The * Quantifier
# --------------------------------------------------

# * means zero or more occurrences.

text = "ac abc abbc"

result = re.findall(r"ab*c", text)

print(result)

# Output:
# ['ac', 'abc', 'abbc']


# --------------------------------------------------
# 15. The ? Quantifier
# --------------------------------------------------

# ? means zero or one occurrence.

text = "color colour"

result = re.findall(r"colou?r", text)

print(result)

# Output:
# ['color', 'colour']


# --------------------------------------------------
# 16. The . Character
# --------------------------------------------------

# A dot matches almost any single character.

text = "cat cot cut"

result = re.findall(r"c.t", text)

print(result)

# Output:
# ['cat', 'cot', 'cut']


# --------------------------------------------------
# 17. The ^ Symbol
# --------------------------------------------------

# ^ means that the pattern should occur
# at the beginning.

text = "Python is easy"

result = re.findall(r"^Python", text)

print(result)

# Output:
# ['Python']


# --------------------------------------------------
# 18. The $ Symbol
# --------------------------------------------------

# $ means that the pattern should occur
# at the end.

text = "I love Python"

result = re.findall(r"Python$", text)

print(result)

# Output:
# ['Python']


# --------------------------------------------------
# 19. The {n} Quantifier
# --------------------------------------------------

# {n} means exactly n occurrences.

text = "1234567890"

result = re.findall(r"\d{4}", text)

print(result)

# Output:
# ['1234', '5678']


# --------------------------------------------------
# 20. Extracting Numbers from Text
# --------------------------------------------------

text = "I bought 5 books, 2 pens and 10 notebooks."

numbers = re.findall(r"\d+", text)

print(numbers)

# Output:
# ['5', '2', '10']


# The values returned by findall() are strings.
# We can convert them into integers.

numbers = [int(num) for num in re.findall(r"\d+", text)]

print(numbers)

# Output:
# [5, 2, 10]


# --------------------------------------------------
# 21. Extracting Words
# --------------------------------------------------

text = "Python is fun"

words = re.findall(r"\w+", text)

print(words)

# Output:
# ['Python', 'is', 'fun']


# --------------------------------------------------
# 22. Extracting Hashtags
# --------------------------------------------------

text = "I am learning #Python #Coding today"

hashtags = re.findall(r"#\w+", text)

print(hashtags)

# Output:
# ['#Python', '#Coding']


# --------------------------------------------------
# 23. Extracting Phone Numbers
# --------------------------------------------------

text = "Contact numbers: 9876543210 and 9123456780"

numbers = re.findall(r"\b\d{10}\b", text)

print(numbers)

# Output:
# ['9876543210', '9123456780']


# --------------------------------------------------
# 24. Basic Email Pattern
# --------------------------------------------------

email = "student@gmail.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")


# --------------------------------------------------
# 25. Raw Strings
# --------------------------------------------------

# Regex patterns commonly use raw strings.

pattern = r"\d+"

print(re.findall(pattern, "I have 25 apples"))

# Raw strings make regex patterns easier to read.


# 26. Common Regex Symbols


# \d   -> digit
# \w   -> word character
# \s   -> whitespace
# +    -> one or more
# *    -> zero or more
# ?    -> zero or one
# .    -> almost any character
# []   -> character set
# ^    -> beginning
# $    -> end
# {n}  -> exactly n occurrences
# |    -> OR
# ()   -> group
# 27. Common re Functions
 re.search()   -> searches anywhere
 re.match()    -> checks from beginning
 re.findall()  -> finds all matches
 re.sub()      -> replaces matches
 re.split()    -> splits using a pattern 
