class Arithmetic:
    
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self):
        self.value1=int(input("Enter 1st Number: "))
        
        self.value2=int(input("Enter 2nd Number: ")) 
        
    def Addition(self):
        result = self.value1+self.value2
        return result
    
    def Subtraction(self):
        result = self.value1-self.value2
        return result
    
    def Multiplication(self):
        result = self.value1*self.value2
        return result
    
    def Division(self):
        result = self.value1/self.value2
        return result
    
def main():
        
    obj1 = Arithmetic()
    obj1.Accept()
    Addition=obj1.Addition()
    print("Addition: ",Addition)
    Subtraction=obj1.Subtraction()
    print("Subtraction: ",Subtraction)
    Multiplication=obj1.Multiplication()
    print("Multiplication",Multiplication)
    Division=obj1.Division()
    print("Division",Division)
    print()
    
    obj2 = Arithmetic()
    obj2.Accept()
    Addition=obj2.Addition()
    print("Addition: ",Addition)
    Subtraction=obj2.Subtraction()
    print("Subtraction: ",Subtraction)
    Multiplication=obj2.Multiplication()
    print("Multiplication",Multiplication)
    Division=obj2.Division()
    print("Division",Division)
       
if __name__ == "__main__":
    main()  