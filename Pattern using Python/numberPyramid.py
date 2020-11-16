"""
      1
     222
    33333
   4444444
 """

n = int(input("Enter your number : "))
n = n + 1

for i in range(1,n):
    #for space
    for j in range(n-i):
        print(" ", end="")

    #for * print
    for k in range((2*i)-1):
        print(i, end="")
    print()