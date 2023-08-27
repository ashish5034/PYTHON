class HDFC:
    ROI = 9.5    #class Variable
    
    def __init__(self,Name,Amount): #constructor
        self.AccountHolder = Name    #instance variable
        self.Balance = Amount  #instance variable
        print("Welcome ",self.AccountHolder)
        print("Account gets Successfully created with initial balace:",self.Balance)
    
    def DisplayBalance(self):  #instance method
        print("HELLO",self.AccountHolder)
        print("Your account balance is : ",self.Balance)
    
    @classmethod    #Decorator
    def DisplayBankInfo(cls): #class method
        print("Welcome to HDFC bank portal")
        print("Our bank is PVT LTD Bank")
        print("We provide ROI on saving account is: ",cls.ROI)
        
    @staticmethod
    def DisplayKYCInfo():
        print("Accordint to the rules of RBI You should provide below documents for KYC")
        print("Your Adhar Card")
        print("Your PAN Card")
        print("Your Passport size photo")
    
    def Withdraw(self,Amount):  #instance method
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance = self.Balance - Amount
            print("Amount Withdraw Successfully...")
            
    def Deposit(self,Amount): #instance method
        self.Balance = self.Balance + Amount
        print("Amount Deposit Succesfully...")

def main():
    print("ROI of HDFC bank is: ",HDFC.ROI)
    
    HDFC.DisplayBankInfo()
    HDFC.DisplayKYCInfo()
    
    print("Creating new account...")
    Amit = HDFC("Amit",5000)   #obj1 __init__(Address=100,"Amit",5000)
    
    print("Creating new account...")
    Sagar = HDFC("Sagar",3000)    #obj2 __init__(Address=200,"Sagar",3000)
    
    print("Performing operations on Amit's Account")
    Amit.Deposit(2000)
    Amit.DisplayBalance()
    
    Amit.Withdraw(1000)
    Amit.DisplayBalance()
    
    print("Performing operations on Sagar's Account")
    Sagar.Deposit(4000)
    Sagar.DisplayBalance()
    
    Sagar.Withdraw(500)
    Sagar.DisplayBalance()
    
if __name__ == "__main__":
    main()