# tuple
my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
print(my_tuple + (4, 5))
print(my_tuple * 2)
print(2 in my_tuple)
print(my_tuple.index(2))
print(my_tuple.count(2))
for item in my_tuple:
    print(item)
# nested tuple
nested_tuple = (1, (2, 3), 4)      