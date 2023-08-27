def pattern(no):
    # for row
    for i in range(no):
    
    # for pattern
        for j in range(no):
            print("*", end=' ')
        print()


def main():
    n = int(input("Enter Number :"))
    pattern(n)
    
if __name__ =="__main__":
    main()