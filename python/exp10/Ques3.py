class product:
    def __init__(self,pid,pname,q,price):
        self.pid=pid
        self.pname=pname
        self.q=q
        self.price=price
    def total(self):
        self.ta=self.q*self.price
    def disp(self):
        print(self.pid,self.pname,self.q,self.price,self.ta)

obj=product(100,"books",12300)
obj.total()
obj.disp()