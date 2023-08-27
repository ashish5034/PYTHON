from functools import reduce

chkEven = lambda no: (no%2==0)
square = lambda no: (no*no)
addition = lambda no1,no2: (no1+no2)

# def chkEven(no):
#     result=[]
#     for val in no:
#         if val%2==0:
#             result.append(val)
#     return result  
  
# def square(no):
#     result = []
#     for val in no:
#         val=val**2
#         result.append(val)
#     return result  

# def Addition(no):
#     sum = 0
#     for val in no:
#         sum = sum+val
#     return sum

def main():
    data = []
    size = int(input("Enter size of list: "))
    for i in range (size):
        value = int(input())
        data.append(value)
    print("Input List = ",data)
    
    output = list(filter(chkEven,data))
    print("List after filter: ",output) 
    
    mOutput = list(map(square,output))
    print("List after map: ",mOutput)
    
    rOutput = reduce(addition,mOutput)
    print("output of reduce: ",rOutput)
    
    # EvenNo=chkEven(data)
    # print("List after filter:",EvenNo)
    
    # squareNo = square(EvenNo)
    # print("List after map: ",squareNo)
    
    # addNo = Addition(squareNo)
    # print("output of reduce: ",addNo)
    
if __name__ =="__main__":
    main()