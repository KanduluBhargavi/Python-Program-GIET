num=int(input("enter a number"))
temp=num
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
if rev==temp:
    print("palindrome")
else:
    print("not a palindrome")