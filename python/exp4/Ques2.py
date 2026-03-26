num=int(input("enter a number"))
n=2
while n<=num//2:
    if num%2==0:
        print("not a prime number")
        break
    n=n+1
else:
    print("prime")