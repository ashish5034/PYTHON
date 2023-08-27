def displayFactors(Value):
    
    for n in range (1, Value):
        if(Value%n==0):
            print(n)
            
def main():

    print("Enter Number : ")
    No = int(input())
    displayFactors(No)
    
if __name__ =="__main__":
    main()