"""
     *
    ***
   *****
  *******
 *********
***********

"""

n = int(input("Enter your number: "))
for i in range(1,n+1):
    #for space
    for j in range(n-i):
        print(" ", end="")

    #for * print
    for k in range((2*i)-1):
        print("*", end="")
    print()