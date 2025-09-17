# dictionaries
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict["age"] = 31
print(my_dict)
my_dict["job"] = "Engineer"
print(my_dict)
del my_dict["city"]
print(my_dict)
my_dict.pop("job")
print(my_dict)
my_dict.clear()
print(my_dict)

x = {}
x['name']= 'jackson'
x['age']=4
x['age']=6
print(x)
x.pop('name')
print(x)
if 'name' in x:
    print("Key exists")
else:
    print("Key does not exist")
