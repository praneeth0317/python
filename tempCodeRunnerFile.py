
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(n):
                if j<=i:
                    print(i-j+1,end="")
    print()
