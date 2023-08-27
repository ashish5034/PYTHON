
def Add(Elements):
    sum = 0
    for val in Elements:  #value in arr[values...]
        sum = sum + val
    return sum

def main():
    Data = []
    
    Size = int(input("Enter No of elements : "))
    
    print("Enter the elements : ")
    
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
        
    print("Input Elements:",Data)
    
    result = Add(Data)
    
    print("Output After Addition :",result)
    
if __name__ == "__main__":
    main()