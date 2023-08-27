
# Function accept more parameter and return parameter
def Marvellous(value1,Value2):
    if (value1>Value2):
        return value1
    else:
        return Value2
    

def main():
    Ret = Marvellous(78,45)
    print("Largest Number is : ",Ret)
    
    Ret = Marvellous(34,99)
    print("Largest Number is : ",Ret)
    
if __name__ == "__main__":
    main()