n=int(input("enter"))
a,b=0,1
print(a,b,end=" ",sep=" ")
c=0
while c<=n:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
