
# Function accept  parameters and  function inside it (Inner function)
def Marvellous(Value1,Value2):
    def Add(A,B):  #inner function
        return A+B
    Ans = Add(Value1,Value2)
    return Ans

def main():
    ret = Marvellous(11,7) 
    print("Addition is : ",ret)
   
if __name__ == "__main__":
    main()