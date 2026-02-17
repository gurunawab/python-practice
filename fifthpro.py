n = int(input("Enter number"))
first = 0
second = 1

if n < 0:
    print("positive number")
else:
    print("First")
    print("Second")

    for i in range(2, n):
        next_term = first + second
        print(next_term)

        first = second
        second = next_term    

n = int(input())

if n < 0:
    print("factorial not defined for negative numbers")
else:
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        print("factorial of", n, "is:", fact)

n = int(input("Enter number:"))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("factorial:", fact)    

n = int(input("Enter numbers is: "))
total = 0

num = abs(n)

while num > 0:
    digit = num % 10
    total = total * 10 + digit
    num = num // 10

if num < 0:
    total = -total
    
print("Reversed Number: ", total) 

n = int(input("Enter number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, n):
        if n % 2 == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not prime")                

n = int(input("Enter number: "))

first = 0
second = 1

if n <= 0:
    print("Enter positive number")
elif n == 1:
    print(first)
else:
    print(first)
    print(second)

    for i in range(2, n):
        next_term = first + second
        print(next_term)

        first = second
        second = next_term        




