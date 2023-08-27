def pattern6(num):
    
    for i in range(1,num+1):
        for j in range(i-1,num,1):
            print("*",end=" ")
        print()

def main():
    
    no = int(input("Enter Input Number: "))
    pattern6(no)
    
if __name__ == "__main__":
    main()