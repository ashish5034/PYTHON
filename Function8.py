def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

# Function accept  parameter and call another function from it and return multiple values
def Marvellous(value1,Value2):
    Ans1=Add(value1,Value2)
    Ans2=Sub(value1,Value2)
    return Ans1,Ans2

def main():
   Arr=Marvellous(11,7)
   print("Addition: ",Arr[0])
   
   print("Addition: ",Arr[1])
    
if __name__ == "__main__":
    main()