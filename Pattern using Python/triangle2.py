"""
* * * * * * * * 
* * * * * * *
* * * * * *
* * * * * 
* * * *
* * *
* *
*
"""
n = int(input("Enter height of the triangle : "))

n = n + 1
for i in range(1, n):
    for j in range(i, n):
        print("* ", end="")

    print()