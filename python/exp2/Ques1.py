p=int(input("enter the principle amount"))
r=float(input("enter rate of interest"))
t=int(input("enter the time"))
si=(p*r*t)/100
print("simple Interest",si)
ci=p*(1+r/100)**t-p
print("compound interest",ci)