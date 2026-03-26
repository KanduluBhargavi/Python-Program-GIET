d1={}
n=int(input("enter no .of key value pairs"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    d1[key]=value
d2={value:key for key, value in d1.items()}
print(d1)
print(d2)