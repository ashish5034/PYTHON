import marvellous 

def main():
    Value1 = int(input("Enter 1st Number : "))
    Value2 = int(input("Enter 2nd Number : "))
    Result = 0 
    Result = marvellous.Addition(Value1,Value2)
    print("Addition is : ", Result)
    
    Result = marvellous.Substraction(Value1,Value2)
    print("Substraction is : ", Result)
    
    Result = marvellous.Multiplication(Value1,Value2)
    print("Multiplication is : ", Result)

if __name__ == "__main__":
    main()