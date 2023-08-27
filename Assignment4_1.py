
from functools import reduce


square = lambda Num: Num*Num


def main():
    Number=int(input("Enter Number: "))
    
    result = square(Number)
    print("Square of Number is: ",result)
    
if __name__ == "__main__":
    main()