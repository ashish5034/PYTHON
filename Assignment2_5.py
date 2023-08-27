def primeNo(num):
    for i in range(2,num):
        if (num%i!=0):
            print("It is Prime Number")
            break
        else:
            print("It is Not Prime Number")
            break
    else:
        print("It is Not prime Number")   

def main():
    
    no = int(input("Enter Number: "))
    primeNo(no)
    
if __name__ == "__main__":
    main()