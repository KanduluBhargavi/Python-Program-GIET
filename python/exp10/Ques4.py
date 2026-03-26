class bank:
    def __init__(self,ano,acc_holder):
        self.ano=ano
        self.acc_holder=acc_holder
        self.bal=0

    def deposit(self,amt):
        self.bal=self.bal+amt
        print(self.bal)
    def withdraw(self,amt):
        if self.bal<0 or self.bal<amt:
            print("no balance")
        else:
            self.bal=self.bal-amt
            print("remianing",self.bal)

obj=bank(101,"ravi")
obj.deposit(500)