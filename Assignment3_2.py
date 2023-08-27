def Max(Element):
    # for val in Element:
    #     if(val>val+1):
    #         return max
    max(Element)
def main():
    
    Data = []
    
    Size = int(input("Enter size of List of Elements: "))
    
    print("Enter Elements: ")
    for i in range(Size):
        Value =int(input())
        Data.append(Value)
    print("Input elements: ",Data)
    
    maximumNo = Max(Data)
    print("Output: ",maximumNo)
    
if __name__ == "__main__":
    main()                