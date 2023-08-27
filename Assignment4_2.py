
from functools import reduce

multiplication = lambda Num1,Num2: Num1*Num2


def main():
    Number1=int(input("Enter Number1: "))
    Number2=int(input("Enter Number2: "))
    
    mult = multiplication(Number1,Number2)
    print(f"Multiplication of {Number1} and {Number2} is: ",mult)
    
if __name__ == "__main__":
    main()