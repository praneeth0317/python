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
