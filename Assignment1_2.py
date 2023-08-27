def ChkNum(number):
    
    if (number %2 == 0):
        print("Even number")
    else:
        print("Odd number")


def main():
    
    print("Enter Number : ")
    No = int(input())
    
    ChkNum(No)
    
if __name__ == "__main__":
    main()