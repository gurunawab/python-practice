for i in range(1, 5):
    for j in range(i, 5):
        print(i, end='')
    print()    

for i in range(1, 10):
    if i == 3 or i == 6:
        continue
    print(i)

for letter in "GeeksForGeeksThat":
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter is: ', letter)

for i in range(1, 5):
    print(i)
    break
else:
    print("No Break")    

def contains_even_number(l):
    for i in l:
        if i % 2 == 0:
            print("List contains an even number")
            break
    else:
        print("List does not contain an even number")

print("for List1: ")
contains_even_number([1, 9, 8])
print("\nfor List2: ")
contains_even_number([1, 9, 7])

items = input("Enter shopping items separated by commas: ").split(',')

for item in items:
    print("Buy: ", item.strip())

n = int(input("Enter number: "))

for i in range(1, n + 1):
    print("Square of", i, "is", i**2)

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print("Time left: ", seconds)
    seconds -= 1

total = 0
num = int(input("Enter number (o to stop): "))
while num != 0:
    total += num 
    num = int(input("Enter number (0 to stop): "))
print("Total sum: ", total)    

n = 3

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i * j, end =' ')
    print()    
