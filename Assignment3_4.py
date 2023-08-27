def frequency(element,no1):
    count ={}
    for i in element:
        if (no1==i):
            count[i] =count.get(i, 0) + 1
    return count

def main():
    
    Data =[]
    Size = int(input("Enter size of list: "))
    print("Enter elements: ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("Input Elemnts: ",Data)
     
    search = int(input("Enter element to search: "))
    ret = frequency(Data,search)
    print(ret)
    
if __name__ == "__main__":
    main()