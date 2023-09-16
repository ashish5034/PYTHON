def pattern(no):               #pattern using for loop
    for i in range(no):
        print(i+1,end=" ")
        
i =1                           #global variable i
    
def recPattern(no):            #pattern using recursion and global variable
    
    global i
    if (i<=5):
        print(i,end=" ")
        i = i+1
        recPattern(no)
        
def main():                     
    
    n=int(input("Input: "))
    pattern(n)
    print(" ")
    recPattern(n)
    
if __name__ =="__main__":
    main()  