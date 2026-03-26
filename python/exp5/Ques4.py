lst=[]
n=int(input("enter no of elements"))
for i in range(n):
    lst.append(int(input()))
lst=list(set(lst))
lst.sort()
print(lst)