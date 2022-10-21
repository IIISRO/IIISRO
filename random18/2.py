class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.number=accountNumber
        self.name=name
        self.balance=balance
    def deposit(self, d):
        print(f'+{d}azn')
        self.balance+=d
        print(f'Balans: {self.balance}azn')
    def withdrawal(self,w):
        print(f'-{w}azn')
        self.balance-=w
        print(f'Balans: {self.balance}azn')

    def bankFees(self):
        self.balance=(95/100)*self.balance
        return self.balance  

    def display(self):
        print('Deposit: ',end="")
        self.deposit(5)   
        print("Withdrawal: ",end="")
        self.withdrawal(10)
        print("Bankfees: ",self.bankFees())
        print("Name: ",self.name)
        print("Number: ", self.number)

obj=BankAccount(1231,"Akif",100)

obj.display()

