
# Function accept multiple parameter and return multiple parameter
def Marvellous(value1,Value2):
    Addition = value1 + Value2
    SubStraction = value1 - Value2
    Multiplication = value1 * Value2
    
    return Addition,SubStraction,Multiplication

def main():
    ret = Marvellous(11,6)
    print("Addition is : ",ret[0])
    print("Substraction is : ",ret[1])
    print("Multiplication is : ",ret[2])
    
if __name__ == "__main__":
    main()