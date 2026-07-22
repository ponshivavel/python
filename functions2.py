1. Function Without Parameters
def greet():
    print("Hello")
    print("Welcome")

greet()
Output
Hello
Welcome
2. Function With Parameters
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")
Output
Hello Alice
Hello Bob

Here, name is a parameter.

3. Function With Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
Output
30

return sends the result back to the caller.

4. Function Without Return
def add(a, b):
    print(a + b)

add(10, 20)

Output

30

Difference:

print() displays the result.
return gives the value back so you can store or reuse it.
5. Default Parameters
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("John")
Output
Hello Guest
Hello John
6. Keyword Arguments
def student(name, age):
    print(name, age)

student(age=20, name="Rahul")
Output
Rahul 20

Order doesn't matter because argument names are used.

7. Positional Arguments
def student(name, age):
    print(name, age)

student("Rahul", 20)
Output
Rahul 20

Order does matter.

8. Variable-Length Arguments (*args)
def total(*numbers):
    print(numbers)
    print(sum(numbers))

total(10, 20, 30)
Output
(10, 20, 30)
60

*args collects multiple positional arguments into a tuple.

9. Keyword Variable Arguments (**kwargs)
def details(**data):
    print(data)

details(name="Alice", age=21)
Output
{'name': 'Alice', 'age': 21}

**kwargs collects keyword arguments into a dictionary.

10. Recursive Function

A function calling itself.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
Output
120
11. Lambda Function (Anonymous Function)
square = lambda x: x * x

print(square(5))
Output
25
