class employee:
    def __init__(self,empid,ename,bp):
        self.empid=empid
        self.ename=ename
        self.bp=bp
        self.ta=0
        self.da=0
        self.gp=0
    def calc(self):
        self.ta=self.bp*10/100
        self.da=self.da*40/100
        self.gp=self.bp+self.ta+self.da
    def disp(self):
        print(self.empid,self.ename,self.bp,self.ta,self.da,self.gp)   

obj=employee(101,"ravi",12000)
obj.calc()
obj.disp()     