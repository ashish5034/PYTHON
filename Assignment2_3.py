# factorial of given input number 

def factorial(Num):
    
    if (Num==0 or Num==1):
        return 1
    else:
        return Num*factorial(Num-1)
    
    
def main():
    
    No=int(input("Enter The Number: "))
    print(f"Factorial of {No} is:",factorial(No))
    
if __name__ == "__main__":
    main()