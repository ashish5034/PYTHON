def Min(Element):
    return min(Element)
    
def main():
    
    Data =[]
    size=int(input("Enter size of list: "))
    
    print("Enter Elements: ")
    for i in range(size):
        Value = int(input())
        Data.append(Value)
    print("Input elements : ",Data)
    
    minimumNo = Min(Data)
    print("Output",minimumNo)
    
if __name__ == "__main__":
    main()