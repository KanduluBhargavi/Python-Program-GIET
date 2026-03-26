class add:
    def addition(self,data1,data2):
        print(data1+data2)
class sub:
    def subtraction(self,data1,data2):
        print(data1-data2)
class mul:
    def multiplication(self,data1,data2):
        print(data1*data2)
class div:
    def division(self,data1,data2):
        if data2!=0:
            print(data1/data2)
        else:
            print("not possible")
class der_class(add,sub,mul,div):
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
obj=der_class()
obj.data1=10
obj.data2=12
obj.addition(obj.data1,obj.data2)
obj.subtraction(obj.data1,obj.data2)
obj.multiplication(obj.data1,obj.data2)
obj.division(obj.data1,obj.data2)
