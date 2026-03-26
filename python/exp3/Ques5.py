sub1=float(input("enter subject 1 marks"))
sub2=float(input("enter subject 2 marks"))
sub3=float(input("enter subject 3 marks"))
sub4=float(input("enter subject 4 marks"))
sub5=float(input("enter subject 5 marks"))
total=sub1+sub2+sub3+sub4+sub5
per=(total/250)*100
if per>=90 and per<=100:
    print("grade O")
elif per>=80 and per<90:
    print("grade E")
elif per>=70 and per<80:
    print("grade A")
elif per>=60 and per<70:
    print("grade B")
elif per>=50 and per<60:
    print("grade C")
else:
    print("grade F")