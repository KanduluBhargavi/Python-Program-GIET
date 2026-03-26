a,b=0,1
even_sum=0
while a<=1000:
    print(a,end=" ")
    if a%2==0:
        even_sum+a
    a,b=b,a+b
print(even_sum)