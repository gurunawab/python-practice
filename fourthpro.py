def add_numbers(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
    
print(add_numbers(1, 2, 3))    

n = int(input("Enter Number is: "))
total = 0

num = abs(n)

while num > 0:
    digit = num % 10
    total = total * 10 + digit
    num = num // 10

if n < 0:
    total = -total

print("Reversed numbers: ", total) 

def myFun(*args, **kwargs):
    print("None Keyword Arguments (*args): ")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs): ")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('hey', 'Welcome', first='Geeks', mid='for', last='Geeks')              

def f1():
    s = 'I love Geeksforgeeks'
    def f2():
        print(s)

    f2()
f1()        

n = int(input("Enter numbers: "))
sqaure = lambda x: x ** 2
print(sqaure(n))

def myfun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myfun(lst)
print(lst)

def myfun2(x):
    x = 20

a = 10
myfun2(a)
print(a)    

n = int(input("Enter number is: "))
 
if n <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime")         


n = int(input("Enter number: "))

if n < 0:
    print("factorial not defined for positive number")
else:
    fact = 1

    for i in range(1, n + 1):
        fact *= i
    print("factorial of", n, "is:", fact)    

string = input("Enter String: ")

count = 0

for ch in string:
    if ch.lower() in "aeiou":
        count += 1
print("Total vowels:", count)        

