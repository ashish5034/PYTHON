
# Function defines another function inside it return as its return value 
def Demo():
    def Add(A,B):
        return A+B
    
    return Add    

def main():
    ret = Demo() 
    ans = ret(10,7)
    print("Addition is : ",ans)
   
if __name__ == "__main__":
    main()