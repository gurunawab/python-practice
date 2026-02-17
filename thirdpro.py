def isFun():
    print("hello World")

isFun()    

def isEvenOdd(num):
    if (num % 2 == 0):
        print("This is Even Number: ", num)
    else:
        print("This is Odd Number: ", num)

num = int(input("Enter Number is: "))
print(isEvenOdd(num))    

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(15)    

def name(fname, lname):
    print(fname, lname)

name(fname='vicky', lname='kumar')    
name(fname='uday', lname='sain') 

def name(name, age):
    print("My name is ", name)
    print("My age is ", age)

print("Case1:")
name("Vicky", 24)

print("\ncase2:")
name(24, "vicky")

  
        

