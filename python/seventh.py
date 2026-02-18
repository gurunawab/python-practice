numbers = [10, 45, 28, 55]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is: ", largest)

list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = []

for num in list1:
    if num not in list2:
        list2.append(num)

print("List after removing duplicates: ", list2)      

rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()    

def fun(*args):
    return sum(args)

print(fun(5, 10, 15))

def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)       

def myfun(*argv):
    for arg in argv:
        print(arg)

myfun('hello', 'welcome','to', 'geeksforgeeks' )   

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4, 66))        

def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)

fun(s1='python', s2='is', s3='awesome', s4='choice')        

def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

print(introduce(Name="ALice", Age=25, City="New York"))    

a = "GeeksForGeeksWebsite"
upper = lambda x: x.upper()
print(upper(a))

check = lambda x: "positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))
print(check(-3))
print(check(0))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))
print(check(7))

func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))

a = [1, 2, 3, 4, 5, 6]
double = map(lambda x: x * 2, a)
print(list(double))

from functools import reduce
a = [1, 2, 3, 4, 5, 6]
mul = reduce(lambda x, y: x * y, a)
print(mul)

def sqaure(x):
    return x * x

numbers = [1, 2, 3, 4, 5, 6]

result = map(sqaure, numbers)

print(list(result))

numbers = [1, 2, 3, 4, 5, 6]

result = map(lambda x: x*x, numbers)

print(list(result))

alpha = ['rahul', 'tanmay', 'ashish', 'devil']

result = map(str.upper, alpha)

print(list(result))

a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)

print(list(result))

