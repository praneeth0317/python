# Strings are sequences of Unicode characters enclosed in single, double, or triple quotes.
single_quote = 'Hello, World!'
double_quote = "Hello, World!"
triple_quote = '''Hello, World!'''
triple_double_quote = """Hello, World!"""
# Strings can be concatenated using the + operator.
greeting = single_quote + " How are you?"
# Strings can be repeated using the * operator.
echo = "Echo! " * 3
# Strings support indexing and slicing.
first_char = single_quote[0]
substring = single_quote[0:5]
# Strings have many built-in methods for manipulation.  
upper_case = single_quote.upper()
lower_case = single_quote.lower()
title_case = single_quote.title()
replaced = single_quote.replace("World", "Python")
# Strings can be formatted using f-strings (Python 3.6+).
name = "Alice"
age = 30
formatted = f"My name is {name} and I am {age} years old."
# Strings can also be formatted using the format() method.
formatted_method = "My name is {} and I am {} years old.".format(name, age)
# Escape sequences can be used to include special characters.
escaped = "He said, \"Hello!\"\nNew line here."
# Raw strings treat backslashes as literal characters.
raw = r"This is a raw string with a backslash: \n"
# Multiline strings can be created using triple quotes.
multiline = """This is a
multiline string.
It can span multiple lines."""  
# Strings are immutable, meaning they cannot be changed after creation.
# However, new strings can be created from existing ones.
immutable_example = single_quote.replace("World", "Everyone")
# Strings can be checked for membership using the 'in' keyword.
is_member = "Hello" in single_quote
# Strings can be split into lists using the split() method.
words = single_quote.split()
# Strings can be joined from lists using the join() method.
joined = " ".join(words)
# Strings can be stripped of whitespace using the strip() method.
whitespace_str = "   Hello, World!   "
stripped = whitespace_str.strip()
# Strings can be checked for certain properties using methods like isalpha(), isdigit(), etc.
is_alpha = "Hello".isalpha()    
is_digit = "12345".isdigit()
