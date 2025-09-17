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