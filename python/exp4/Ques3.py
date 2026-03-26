a=int(input("enter number 1"))
b=int(input("enter number 2"))
c=int(input("enter number 3"))
i=1
gcd=1
while i<=a and i<=b and i<=c:
    if a%i==0 and b%i==0 and c%i==0:
        gcd=i
    i=i+1
print(gcd)