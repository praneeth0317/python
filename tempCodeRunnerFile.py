l = ["bat", "ball", "glove"]
for item in l:
    print("Item:", item)

for char in "hello":
    print("Character:", char)

x = "hey there"
for _ in x:
    print("Character:", _)

t = (56, "name", 5.4)
for i in t:
    print(i)

count = 0
for i in range(10):
    count += 1
print("Total count:", count)

d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
for key, value in d.items():
    print("%s  %d" % (key, value))
for key in d.keys():
    print("Key:", key)
for value in d.values():
    print("Value:", value)
for index, value in enumerate(l):
    print("Index:", index, "Value:", value)
for index, char in enumerate("hello"):
    print("Index:", index, "Character:", char)
for index, item in enumerate(t):
    print("Index:", index, "Item:", item)
for index, (key, value) in enumerate(d.items()):
    print("Index:", index, "Key:", key, "Value:", value)