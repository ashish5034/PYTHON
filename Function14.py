
# Function defines another function inside it return as its return value 
def Demo(val1,val2):
    def Add(A,B):
        return A+B
    
    return Add(val1,val2)  

def main():
    ret = Demo(10,7) 
   
    print("Addition is : ",ret)
   
if __name__ == "__main__":
    main()