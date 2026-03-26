para=input("enter")
wc=len(para.split(" "))
pc=0
for i in para.split(" "):
    if i==i[::-1]:
        pc=pc+1
    print(i[::-1],end=" ")

print(pc,wc)