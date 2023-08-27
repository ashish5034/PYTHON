def pattern8(no):
    
    for i in range(1,no+1):
        for j in range(i):
            print(j+1,end=" ")
        print()


def main():
    
    num = int(input("Enter Input No: "))
    pattern8(num)    
    
if __name__ == "__main__":
    main()