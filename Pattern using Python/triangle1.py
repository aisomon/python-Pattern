"""
******
 *****
  ****
   ***
    **
     *
"""


n = int(input("Enter height of the triangle : "))
n = n + 1

#Reverse Mirrored Right Triangle Star Pattern

for i in range(1, n):
    for j in range(1, n):
        if(j < i):
            print(" ", end = "")
        else:
            print("*", end = "")
    print()