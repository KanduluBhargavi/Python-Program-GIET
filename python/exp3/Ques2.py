import math
a=int(input("enter value a"))
b=int(input("enter value b"))
c=int(input("enter value c"))
d=(b**2)-2*a*c
if d==0:
    roots=-b/2*a
    print("real roots are equal",roots)
elif d>0:
    root1=-b+math.sqrt(d)/2*a
    root2=-b-math.sqrt(d)/2*a
    print("root1",root1)
    print("root2",root2)
else:
    print("no real roots")
    