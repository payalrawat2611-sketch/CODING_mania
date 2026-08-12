
# Python Loops

Loops are used to repeat code.

## for Loop

Used to iterate over a sequence.

```python
for i in range(5):
    print(i)


#  while Loop

Runs while a condition is True.

i = 1

while i <= 5:
    print(i)
    i += 1

#  break : Stops the loop.

for i in range(10):
    if i == 5:
        break
continue

Skips the current iteration.

for i in range(5):
    if i == 2:
        continue
    print(i)


#  Keep in mind
range(5) means 0 to 4.
break → exits the loop.
continue → skips the current iteration.
Avoid infinite while loops.