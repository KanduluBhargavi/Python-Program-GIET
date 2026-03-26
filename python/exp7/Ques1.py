m=int(input("enter start number"))
n=int(input("enter end"))
list=list1=[]
for i in range(m,n):
    list.append(i)
    if i%3!=0:
        list1.append(i)
print(sum(list))
print(sum(list)/len(list))
print(max(list))
print(min(list))
print(list1)