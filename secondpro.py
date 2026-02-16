n = 4

for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()            

items = ["apple", "banana", "cherry", "stop", "grape"]

for item in items:
    if item == "stop":
        pass
    print("Current item: ", item)

for i in range(1, 11):
    print(i , end= " ")

i = 10
while i > 0:
    print(i)
    i -= 1

for i in range(1, 50):
    ans = i % 2
    if ans == 0:
        print(i, end =" ")

n = int(input())
total = 0

for i in range(1, n + 1):
    total += i
    
print("Sum of 1 to", n, "is:", total)

n = int(input("Enter number is: "))
count = 0

while n > 0:
    n //= 10
    count += 1

print("Total digits: ", count)    

