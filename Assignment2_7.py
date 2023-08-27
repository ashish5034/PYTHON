def pattern(no):
    for i in range(no):     #Row = Horizontal
        for j in range(no): #column = vertical
            print(j+1,end=" ")
        print()
            
def main():
    
    num = int(input("Enter Input Number: "))
    pattern(num)
    
if __name__ =="__main__":
    main()