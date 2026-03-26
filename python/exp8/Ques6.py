s=input('enter')
def rev(m):
    a=" "
    for i in range(len(m)):
        a=a+(m[len(m)-i-1])
    print(a)
rev(s)