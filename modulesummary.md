# 🐍 Python Notes

---

# 📚 Modules in Python

A **module** is a Python file (`.py`) that contains functions, classes, and variables which can be reused in other programs.

## Types of Modules

### 1. Built-in Modules

Python provides many built-in modules.

#### Math Module

```python
import math

print(math.sqrt(25))      # 5.0
print(math.factorial(5))  # 120
print(math.ceil(2.3))     # 3
print(math.floor(2.9))    # 2
print(math.pi)            # 3.141592653589793
```

> **Note:** `math.ceil()` and `math.floor()` take only **one argument**.

---

#### Random Module

```python
import random

print(random.randint(1, 10))
print(random.choice([10, 20, 30]))
print(random.random())
```

---

#### Datetime Module

```python
import datetime

print(datetime.datetime.now())
print(datetime.date.today())
```

---

#### OS Module

```python
import os

print(os.getcwd())        # Current working directory
print(os.listdir())       # List files
```

---

#### Time Module

```python
import time

print(time.time())
time.sleep(2)
print("Done")
```

---

## 2. User-Defined Modules

You can create your own module.

### mymath.py

```python
def add(a, b):
    return a + b
```

### main.py

```python
import mymath

print(mymath.add(10, 20))
```

---

# 📦 Packages in Python

A **package** is a folder that contains multiple Python modules.

Example:

```
project/
│── main.py
│── mymath.py
│── student.py
│── database.py
```

A package helps organize large projects.

---

# ➜ Next Topic: File Handling

---

# 📁 File Handling in Python

File handling allows Python to create, read, write, append, and delete files.

---

## Opening a File

```python
file = open("filename.txt", "mode")
```

### File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (Default) |
| `"w"` | Write (Creates new or overwrites existing file) |
| `"a"` | Append data |
| `"x"` | Create a new file |
| `"rb"` | Read Binary |
| `"wb"` | Write Binary |

---

## Reading a File

### Read Entire File

```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

---

### Read One Line

```python
file = open("sample.txt", "r")

print(file.readline())

file.close()
```

---

### Read All Lines

```python
file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

---

## Writing to a File

```python
file = open("sample.txt", "w")

file.write("Hello, Python!")

file.close()
```

**sample.txt**

```
Hello, Python!
```

---

## Appending to a File

```python
file = open("sample.txt", "a")

file.write("\nWelcome to File Handling.")

file.close()
```

**Output**

```
Hello, Python!
Welcome to File Handling.
```

---

## Using the `with` Statement (Recommended)

The `with` statement automatically closes the file.

### Reading

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

### Writing

```python
with open("sample.txt", "w") as file:
    file.write("Learning Python")
```

---

## Checking if a File Exists

```python
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File not found")
```

---

## Deleting a File

```python
import os

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted")
else:
    print("File does not exist")
```

---

## Example Program

```python
with open("student.txt", "w") as file:
    file.write("Name: John\n")
    file.write("Age: 20\n")

with open("student.txt", "r") as file:
    print(file.read())
```

**Output**

```
Name: John
Age: 20
```

---

## Exception Handling

```python
try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist.")
```

---

## Best Practices

✔ Use the `with` statement.

✔ Choose the correct file mode.

✔ Handle exceptions using `try-except`.

✔ Close files if you don't use `with`.

---

# ➜ Next Topic: Object-Oriented Programming (OOP)

---

# 🏛️ Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **classes** and **objects**.

---

## Main Concepts of OOP

- Class
- Object
- Constructor
- Methods
- Instance Variables
- Class Variables
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

# 1. Class

A **class** is a blueprint for creating objects.

```python
class Student:
    name = "Pon"
    age = 20
```

---

# 2. Object

An **object** is an instance of a class.

```python
class Student:

    name = "Pon"
    age = 20

s1 = Student()

print(s1.name)
print(s1.age)
```

**Output**

```
Pon
20
```

---

# 3. Constructor (`__init__()`)

A constructor runs automatically whenever an object is created.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("John", 21)

print(s1.name)
print(s1.age)
```

**Output**

```
John
21
```

---

## What is `self`?

`self` refers to the current object.

```python
self.name = name
```

means

```python
object.name = value
```

---

# 4. Methods

Functions inside a class are called **methods**.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Alex")

s1.display()
```

**Output**

```
Student Name: Alex
```

---

# 5. Instance Variables

Instance variables belong to each object.

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
c2 = Car("Audi")

print(c1.brand)
print(c2.brand)
```

**Output**

```
BMW
Audi
```

Each object stores its own data.

---

# 6. Class Variables

Class variables are shared by all objects.

```python
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

s1 = Student("Ram")
s2 = Student("John")

print(s1.college)
print(s2.college)
```

**Output**

```
ABC College
ABC College
```

---
