try:
    raise ArithmeticError("Arithmetic error occured")
except ArithmeticError as e:
    print(e)


try:
    result = 10/ 0
except ZeroDivisionError as e:
    print(e)    

import math
try:
    result = math.exp(1000)
except OverflowError as e:
    print(e)   

try:
    open("non_existent_file.txt")
except FileNotFoundError as e:
    print("FileNotFoundError caught:", e)
except OSError as e:
    print("OSError caught:", e)       

try:
    print(var)
except NameError as e:
    print(e)  

try:
    li = [1] * (10**10)
except MemoryError as e:
    print(e)        

d = {"key1": "value1"}

try:
    val = d["key2"]
except KeyError as e:
    print(e)

my_list = [1, 2, 3]

try:
    element = my_list[5]
except IndexError as e:
    print(e) 

class MyClass:
    pass

obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)   

try:
    assert 1 == 2, "Assertion failed"
except AssertionError as e:
    print(e)  

import numpy as np
np.seterr(all='raise')

try:
    np.divide(1, 0)
except FloatingPointError as e:
    print("FloatingPointError caught:", e)    

try:
    x = int(input())
    print(10 / x)
except (ValueError, ZeroDivisionError):
    print("Invalid input")  

try:
    x = 10 / 0
except Exception as e:
    print("Error:", e)  

