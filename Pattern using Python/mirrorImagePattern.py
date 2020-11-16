"""
A            A
AA          AA
AAA        AAA
AAAA      AAAA
AAAAA    AAAAA
AAAAAA  AAAAAA
"""

n = int(input("Enter a number : "))

n = n +1
for i in range(1, n):
    flag = 0
    for j in range(i):
        print("A", end="")
    for k in range(((n-i)*2)-flag):
        print(" ", end="")
    for l in range(i):
        print("A", end="")
    print()
