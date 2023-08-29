class HDFC:
    ROI = 10.5                                                        #class Variable
    
    def __init__(self, Name, Amount):                                 #constructor
        
        self.AccountHolder = input("Enter Name Of AccountHolder: ")   #instance variable
        self.Balance = int(input("Enter Amount Rs: "))                #instance variable
        print("Welcome ",self.AccountHolder)
        print("Account gets Successfully created with initial balance Rs:",self.Balance)
        
        
    def DisplayBalance(self):                                         #instance method
        
        print("HELLO",self.AccountHolder)
        print("Your account balance is : ",self.Balance)
    
    @classmethod                                                      #Decorator
    def DisplayBankInfo(cls):                                         #class method
        print("Welcome to HDFC bank portal")
        print("Our bank is PVT LTD Bank")
        print("We provide ROI on saving account is: ",cls.ROI)
        
    @staticmethod
    def DisplayKYCInfo():
        print("Accordint to the rules of RBI You should provide below documents for KYC")
        print("Your Adhar Card")
        print("Your PAN Card")
        print("Your Passport size photo")
    
    def Withdraw(self,Amount):                                        #instance method
        Amount = int(input("Enter Amount To Withdraw: "))
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance = self.Balance - Amount
            print("Amount Withdraw Successfully...")
            
    def Deposit(self,Amount):                                         #instance method
        Amount = int(input("Enter Amount To Deposit: "))
        self.Balance = self.Balance + Amount
        print("Amount Deposit Succesfully...")

def main():
    print("ROI of HDFC bank is: ",HDFC.ROI)
    
    HDFC.DisplayBankInfo()
    HDFC.DisplayKYCInfo()
    
    print("Creating new account...")
    obj1 = HDFC("obj1",5000)                                         #obj1 __init__(Address=100,"obj1",5000)
    
    print("Creating new account...")
    obj2 = HDFC("obj2",3000)                                         #obj2 __init__(Address=200,"obj2",3000)
    
    print(f"Performing operations on {obj1.AccountHolder} Account")
    obj1.Deposit(2000)
    obj1.DisplayBalance()
    
    obj1.Withdraw(1000)
    obj1.DisplayBalance()
    
    print(f"Performing operations on {obj2.AccountHolder} Account")
    obj2.Deposit(4000)
    obj2.DisplayBalance()
    
    obj2.Withdraw(500)
    obj2.DisplayBalance()
    
if __name__ == "__main__":
    main()