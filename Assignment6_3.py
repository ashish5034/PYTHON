class Numbers:
    def __init__(self,No):
        self.Value = int(input("Enter the Number: "))
        
    def ChkPrime(self):
    
        for i in range(2,self.Value):
            if(self.Value%i == 0):
                return False
            else:
                return True
        else:
            return False
        
    def Factors(self):
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(f"Factors of {self.Value} is : ",i)
        
    def ChkPerfect(self):
        
        sum = 0
        for i in range(1, self.Value//2 + 1):
            if self.Value % i == 0:
                sum = sum + i
        if sum == self.Value:
            return True
        else:
            return False
        
    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                sum = sum + i
        print(f"Sum of Factors is : ",sum)
        
        
def main():
    
    obj1 = Numbers(1)
    
    print(obj1.ChkPrime())
    obj1.Factors()
    print(obj1.ChkPerfect())
    obj1.SumFactors()

if __name__ == "__main__":
    main()