def factors(num):
    for i in range(1,num):
        if (num % i == 0):
            print(i, end=" ")
            

            
def main():
    
    no = int(input("Enter Number: "))
    factors(no)
    
    
if __name__ == "__main__":
    main()