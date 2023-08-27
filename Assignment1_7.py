def Div(no):
    
    if(no%5==0):
        return True
    else:
        return False

def main():
    print("Enter Number: ")
    Value = int(input())
    
    print(Div(Value))
    
if __name__ == "__main__":
    main()