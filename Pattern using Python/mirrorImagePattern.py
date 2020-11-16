n = int(input("Ener yor number: "))

character = "*"

mid = int((n+1)/2)

for i in range(mid):
    print(" "*i + character*(2*(mid-i)-1))
for j in range(mid-1, 0, -1):
    print(" "*(j-1) + character*(2*(mid-j) + 1))