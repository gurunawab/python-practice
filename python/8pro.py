def starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "cheery", "avocado", "apricot", "adorable"]
res = filter(starts_a, li)
print(list(res))

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, numbers)
print(list(result))


numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))


names = ["rahukl", "tanmay", "shrivastav", "hanumanji", "Savitridevi"]
result = filter(lambda x: len(x) > 5, names)
print(list(result))

from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)

from itertools import accumulate
nums = [1, 2, 3, 4]
result = accumulate(nums)
print(list(result))

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@decorator
def greet():
    print("Hello, World")
greet()    

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b
print(add(5, 3))

def greet(n):
    return f"hello, {n}!"
say_hi = greet
print(say_hi("Alice"))

def apply(f, v):
    return f(v)
res = apply(say_hi, "Bob")
print(res)

def make_mult(f):
    def mult(x):
        return x * f
    return mult
dbl = make_mult(2)
print(dbl(5))

def fun(f, x):
    return f(x)

def square(x):
    return x * x
res = fun(square, 5)
print(res)

def simple_decorator(func):
    def wrapper():
        print(">>> Starting function")
        func()
        print(">>> Function finished")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")
greet()      


def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()


def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass
print(Person.class_name)


class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
res = MathOperations.add(5, 3)
print(res)


class Employee:
    raise_amount = 1.05
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

Employee.set_raise_amount(1.10)
print(Employee.raise_amount)           


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 10
print(c.area)                


def decore1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decore(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decore1
@decore
def num():
    return 10

@decore
@decore1
def num2():
    return 10

print(num())
print(num2())
