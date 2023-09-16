def pattern(no):               #pattern using for loop
    for i in range(no):
        print("*",end=" ")
        
i =1                           #global variable i
    
def recPattern(no):            #pattern using recursion and global variable
    
    global i
    if (i<=5):
        print("*",end=" ")
        i = i+1
        recPattern(no)
    
def stars(no):                 #pattern using recursion
    
    if no <= 0:
        pass
    else:
        print("*", end=" ")
        stars(no - 1)
        
def main():                     
    
    n=int(input("Input: "))
    pattern(n)
    print(" ")
    recPattern(n)
    print(" ")
    stars(n)
    
if __name__ =="__main__":
    main()  