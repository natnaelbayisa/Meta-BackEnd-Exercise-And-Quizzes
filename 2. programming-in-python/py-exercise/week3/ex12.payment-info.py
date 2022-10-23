class Paylips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
        
    def pay(self):
        self.payment = "yes"
          
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet" 
        
#checking status before payment 
a = Paylips("A", "no", 10000)
b = Paylips("B", "no", 10000)
print(a.status(), "\n", b.status())

print("------------------------------------------>")
#checking status after paymentnati.pay()

a.pay()

print(a.status(), "\n", b.status())
