#loops 
for i in range(5):
    print("Iteration:", i)
print("Loop finished")
 
x = 3
for i in range (x):
    print(":", i)

for i in range(1, 10, 2):
    print("Current value:", i)
print("Loop with step finished")

for i in range(0, 15, 1):
    print("current value:", i)

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
#
for key, value in d.items():
    print("%s  %d" % (key, value))
for key in d.keys():
    print("Key:", key)
for value in d.values():
    print("Value:", value)
'''for index, value in enumerate(l):
    print("Index:", index, "Value:", value)
for index, char in enumerate("hello"):
    print("Index:", index, "Character:", char)
for index, item in enumerate(t):
    print("Index:", index, "Item:", item)
for index, (key, value) in enumerate(d.items()):
    print("Index:", index, "Key:", key, "Value:", value)'''

l = ["games", "class", "break"]
for i in range(len(l)):
    print(l[i])

'given a number N need to print multiplication table'
N = 5
for i in range(1, 11):
    print(N * i)
def multiplication_table(N):
    for i in range(1, 11):
        print(N * i)

https://www.geeksforgeeks.org/python/python-for-loops/

# break 
for i in range(15):
    if i == 13:
        break
    print(i)
print("Loop ended")