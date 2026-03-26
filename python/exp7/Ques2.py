li=[]
m=int(input("enter start number"))
n=int(input("enter end number"))
for i in range(m,n):
    for j in range(2,i//2+1):
        if i%j==0:
            break
        else:
            li.append(i)

print(li)