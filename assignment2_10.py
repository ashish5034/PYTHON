def getSum(n):
    
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
   
def main():
    
    n = int(input("Enter Number: "))
    print(getSum(n))
    
if __name__ == "__main__":
    main()