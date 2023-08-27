def displayFactors(No):
    
    n = 1
    while(n < No):
        if(No%n==0):
            print(n)
            n=n+1
            
def main():
    print("Enter Number : ")
    No1 = int(input())
    displayFactors(No1)
if __name__ =="__main__":
    main()