import MarvellousNum
  
def listPrime(No):
    sum = 0
    for n in No:
        # if MarvellousNum.ChkPrime(n):
        sum = sum+n
    return sum    
def main():
    
    Data =[]
    Size = int(input("Enter size of list: "))
    print("Enter elements: ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("Input Elemnts: ",Data)
    data1 = MarvellousNum.ChkPrime(Data)
    print (data1)
    data2 = listPrime(data1)
    print(data2)
if __name__ == "__main__":
    main()