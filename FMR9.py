
from functools import reduce
CheckEven = lambda No :  (No%2==0)   
Increase =lambda No : No + 2
Add = lambda A,B : A + B

# task : name of function
#elements : list of data
def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result
    
def mapX(Task, Elements):
    Result = []
    for no in Elements:
        Ret =Task(no)
        Result.append(Ret)
    return Result

def main():
    Data = []
    
    print("Enter No of elements : ")
    Size = int(input())
    
    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("Input dat:",Data)
    
    output = list(filterX(CheckEven,Data))
    print("Output after filter:",output)
    
    moutput = list(mapX(Increase,output))
    print("Output after Map:",moutput)
    
    result = reduce(Add,moutput)
    print("Output after reduce:",result)
    
if __name__ == "__main__":
    main()