# 🔧 Functions in Python

A **function** is a block of reusable code that performs a specific task.

---

# Function Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

---

# 1. Function Without Parameters

```python
def greet():
    print("Hello")
    print("Welcome")

greet()
```

### Output

```
Hello
Welcome
```

---

# 2. Function With Parameters

```python
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")
```

### Output

```
Hello Alice
Hello Bob
```

### Note

- `name` is called a **parameter**.
- `"Alice"` and `"Bob"` are **arguments**.

---

# 3. Function With Return Value

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### Output

```
30
```

### Note

`return` sends the result back to the caller.

---

# 4. Function Without Return

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Output

```
30
```

### Difference Between `print()` and `return`

| print() | return |
|----------|---------|
| Displays the output | Sends the value back to the caller |
| Cannot be stored | Can be stored in a variable |
| Mainly used for displaying | Used for further calculations |

Example:

```python
def add(a, b):
    return a + b

x = add(10, 20)

print(x * 2)
```

Output

```
60
```

---

# 5. Default Parameters

A default value is used if no argument is passed.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("John")
```

### Output

```
Hello Guest
Hello John
```

---

# 6. Keyword Arguments

Arguments are passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=20, name="Rahul")
```

### Output

```
Rahul 20
```

### Note

The order does **not** matter.

---

# 7. Positional Arguments

Arguments are passed according to their position.

```python
def student(name, age):
    print(name, age)

student("Rahul", 20)
```

### Output

```
Rahul 20
```

### Note

The order **does** matter.

---

# 8. Variable-Length Arguments (`*args`)

`*args` allows a function to accept any number of positional arguments.

```python
def total(*numbers):
    print(numbers)
    print(sum(numbers))

total(10, 20, 30)
```

### Output

```
(10, 20, 30)
60
```

### Note

- `*args` stores values as a **tuple**.

Example

```python
def fruits(*names):
    for name in names:
        print(name)

fruits("Apple", "Banana", "Orange")
```

Output

```
Apple
Banana
Orange
```

---

# 9. Keyword Variable Arguments (`**kwargs`)

`**kwargs` accepts any number of keyword arguments.

```python
def details(**data):
    print(data)

details(name="Alice", age=21)
```

### Output

```
{'name': 'Alice', 'age': 21}
```

### Note

- `**kwargs` stores values as a **dictionary**.

Example

```python
def student(**info):
    for key, value in info.items():
        print(key, ":", value)

student(name="John", age=20, city="Chennai")
```

Output

```
name : John
age : 20
city : Chennai
```

---

# 10. Recursive Function

A recursive function is a function that calls itself.

### Example: Factorial

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

### Output

```
120
```

### How It Works

```
factorial(5)

= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1
= 120
```

---

# 11. Lambda Function (Anonymous Function)

A lambda function is a small function without a name.

### Syntax

```python
lambda arguments : expression
```

### Example 1

```python
square = lambda x: x * x

print(square(5))
```

### Output

```
25
```

---

### Example 2

```python
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```
30
```

---

### Example 3

```python
maximum = lambda a, b: a if a > b else b

print(maximum(15, 20))
```

### Output

```
20
```

---

# 12. Scope of Variables (LEGB Rule)

Python searches variables in this order:

```
Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in
```

### Example

```python
x = 100

def display():
    x = 50
    print(x)

display()

print(x)
```

### Output

```
50
100
```

---

# 13. Built-in Functions

Python provides many built-in functions.

```python
print(len("Python"))
print(max(10, 20, 30))
print(min(10, 20, 30))
print(sum([1, 2, 3, 4]))
print(abs(-10))
print(type(10))
```

### Output

```
6
30
10
10
10
<class 'int'>
```

---


# 📌 Quick Revision

| Topic | Description |
|--------|-------------|
| Function | Reusable block of code |
| Parameter | Variable in function definition |
| Argument | Value passed to the function |
| return | Sends value back |
| print | Displays output |
| Default Parameter | Uses default value if no argument is passed |
| Keyword Argument | Passed using parameter names |
| Positional Argument | Passed according to position |
| *args | Multiple positional arguments (Tuple) |
| **kwargs | Multiple keyword arguments (Dictionary) |
| Recursion | Function calling itself |
| Lambda | Anonymous one-line function |
| Scope | LEGB (Local → Enclosing → Global → Built-in) |
