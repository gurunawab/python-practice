def greet():
    msg = "hello from inside the function"
    print("Inside function: ", msg)

greet()   

message = "Python is very awesome"

def display():
    print("Inside function:", message)

display()
print("Outside function: ", message)    

def fun():
    s = "Me too"
    print(s)

s = "Geeks For geeks"
fun()
print(s)    

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(66))    

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(12))    

def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)
    
def nontail_fact(n):
    if n == 1:
        return 1
    else:
        return n * nontail_fact(n-1)

print(tail_fact(5))
print(nontail_fact(5))   

     


