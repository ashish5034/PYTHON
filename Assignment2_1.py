import Arithmetic

def main():
    Value1 = int(input("Enter 1st Number : "))
    Value2 = int(input("Enter 2nd Number : "))
    Result = 0 
    Result = Arithmetic.Addition(Value1,Value2)
    print("Addition is : ", Result)
    
    Result = Arithmetic.Substraction(Value1,Value2)
    print("Substraction is : ", Result)
    
    Result = Arithmetic.Multiplication(Value1,Value2)
    print("Multiplication is : ", Result)
    
    Result = Arithmetic.Division(Value1,Value2)
    print("Division is : ", Result)

if __name__ == "__main__":
    main()