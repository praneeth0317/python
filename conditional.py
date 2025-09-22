# if conditional statements
a = 33
b = 200
if b > a:
    print("b is greater than a")

# if...else statement
a = 33
b = 200
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b or a is equal to b")

# if...elif...else statement
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif b == a:
    print("a is equal to b")
else:
    print("a is greater than b")

# short hand if
if a > b: print("a is greater than b")
# short hand if...else
a = 20
b = 30
print("a is greater than b") if a > b else print("a is less than b or a is equal to b")

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

x = int(input("Enter a number: "))
if x < 0:
    print("The number is negative.")
if x == 0:
    print("The number is zero.")
if x > 0:
    print("The number is positive.")
if x <= 0:
    print("The number is non-positive.")
if x >= 0:
    print("The number is non-negative.")
if x != 0:
    print("The number is non-zero.")

y = int(input("Enter a number: "))
if y % 2 == 0:
    print("The number is even.")
if y % 2 != 0:
    print("The number is odd.")
if y % 5 == 0:
    print("The number is a multiple of 5.")
if y % 10 == 0:
    print("The number is a multiple of 10.")
if y % 2 == 0 and y % 5 == 0:
    print("The number is a multiple of both 2 and 5.")
if y % 2 == 0 or y % 5 == 0:
    print("The number is a multiple of 2 or 5.")
if not y % 2 == 0:
    print("The number is odd (using not).")
if not y % 2 != 0:
    print("The number is even (using not).")
if not y % 5 == 0:
    print("The number is not a multiple of 5.")
if not y % 10 == 0:
    print("The number is not a multiple of 10.")
if not (y % 2 == 0 and y % 5 == 0):
    print("The number is not a multiple of both 2 and 5.")
if not (y % 2 == 0 or y % 5 == 0):
    print("The number is neither a multiple of 2 nor 5.")
if y > 0 and y % 2 == 0:
    print("The number is a positive even number.")
if y < 0 and y % 2 != 0:
    print("The number is a negative odd number.")
if y >= 0 and y % 5 == 0:
    print("The number is a non-negative multiple of 5.")
if y <= 0 and y % 10 != 0:
    print("The number is a non-positive non-multiple of 10.")
if y > 0 or y % 2 == 0:
    print("The number is either positive or even (or both).")
if y < 0 or y % 5 != 0:
    print("The number is either negative or not a multiple of 5 (or both).")
if y == 0 or y % 10 == 0:
    print("The number is either zero or a multiple of 10 (or both).")
if y != 0 or y % 2 != 0:
    print("The number is either non-zero or odd (or both).")
if not (y > 0 and y % 2 == 0):
    print("The number is not a positive even number.")

t = int(input("enter a number:"))
if t == int(t/2):
    print("yes")
else:
    print("no")
