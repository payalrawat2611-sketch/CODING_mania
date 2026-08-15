# Python Dictionaries


A dictionary stores data in **key-value pairs** and is written using `{}`.


```python
student = {
    "name": "Payal",
    "age": 20,
    "branch": "CSE"
}

Access values using their keys:

print(student["name"])

Add or update values:

student["age"] = 21
student["city"] = "Indore"

Remove a key-value pair:

student.pop("city")

Useful methods:

print(student.keys())
print(student.values())
print(student.items())


# Keep in mind
Dictionaries store key-value pairs.
Keys must be unique.
Values can be of different data types.
Access values using their keys.
Dictionaries are mutable.