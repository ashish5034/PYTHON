# filter map Reduce

from functools import reduce


# def CheckEven(No):
#     return (No%2==0)

CheckEven = lambda No :  (No%2==0)    
    
# def Increase(No):
#     return No + 2
Increase =lambda No : No + 2

# def Add(A,B):
#     return A + B

Add = lambda A,B : A + B
def main():
    Data = []
    
    print("Enter No of elements : ")
    Size = int(input())
    
    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("Input dat:",Data)
    output = list(filter(CheckEven,Data))
    print("Output after filter:",output)
    
    moutput = list(map(Increase,output))
    print("Output after Map:",moutput)
    
    result = reduce(Add,moutput)
    print("Output after reduce:",result)
    
if __name__ == "__main__":
    main()