def CheckPositive(no):
    if(no>0):
        print("Positive Number ")
    elif (no<0):
        print("Negative number ")
    else:
        print("Zero")


def main():
    print("Enter Number: ")
    number = int(input())
    CheckPositive(number)
    
if __name__ == "__main__":
    main()