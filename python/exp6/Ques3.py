sentence="python is easy"
l1=sentence.split()
print("words",l1)
for index,word in enumerate(l1):
    print(index,word)
l2=[1,2,3]
l3=list(zip(l1,l2))
print("combined",l3)