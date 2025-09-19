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