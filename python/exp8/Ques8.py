n1=int(input("enter "))
n2=int(input('enter'))
n3=int(input("enter"))
def maxx(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n3:
        print(n2)
    else:
        print(n3)
maxx(n1,n2,n3)