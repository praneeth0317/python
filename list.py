# List operations
my_list = [1, 2, 3, 4, 5]
print(my_list)
print("Original List:", my_list)
# Append
my_list.append(6)
print(my_list)
# Insert
my_list.insert(0, 0)
print(my_list)
# Remove
my_list.remove(3)
print(my_list)
# Pop
my_list.pop()
print(my_list)
# Slice
print(my_list[1:4])
# Length
print(len(my_list)) 
# Mixed data types
x = [17, 'praneeth', 89.9, True]
print(x)
print(type(x))
print(x[1])
print(x[0:3])
print(x[-1])
x.append('hello')
print(x)
# reverse
x.reverse()
print(x)
# sort
y = [5, 2, 9, 1, 5, 6]
y.sort()
print(y)

# Nested lists
nested_list = [1, 2, [3, 4], [5, 6]]
print(nested_list)
print(nested_list[2])
print(nested_list[2][1])
print(nested_list[3][0])
