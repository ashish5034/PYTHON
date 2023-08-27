
# Function accept multiple parameter and return multiple parameter
def Marvellous(value1,Value2):
    Addition = value1 + Value2
    SubStraction = value1 - Value2
    Multiplication = value1 * Value2
    
    return Addition,SubStraction,Multiplication

def main():
    ret1,ret2,ret3 = Marvellous(11,6)
    print("Addition is : ",ret1)
    print("Substraction is : ",ret2)
    print("Multiplication is : ",ret3)
    
if __name__ == "__main__":
    main()