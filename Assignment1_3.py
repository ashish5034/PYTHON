def Add(Number1, Number2):
    
    addition = Number1 + Number2
    return addition


def main():
    
    print("Enter First Number: ")
    No1 = int(input())
    
    print("Enter Second Number: ")
    No2 = int(input())
    
    print("Addition is : ",Add(No1, No2))
    
    
if __name__ == "__main__":
    main()
    