fruits=["apple","banana","cherry","kiwi"]
for fruit in fruits[::-1]:
    print(fruit)
    print(len(fruit))
rev_fruit=[]
for i in fruits:
    rev_fruit.append(i[::-1])
print(rev_fruit)