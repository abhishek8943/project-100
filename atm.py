class Atm(object):
    def __init__(self,cardnumber,pincode):
        self.cardnumber = cardnumber
        self.pincode = pincode

    def withdraw(self,amount):
        balance=50000-amount
        print(str(amount)+" money has been withdrawn")
    
    def balance(self):
        print("you have 50000 money  in your account")

user=Atm(000-000-000,123456)
user.balance()
user.withdraw(5000)
        
         