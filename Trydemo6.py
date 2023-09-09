
def main():
    try:
        print("Enter First Number:")
        no1 = int(input())

        print("Enter Second Number:")
        no2 = int(input())
        
        Ans = 0
    

        Ans = no1 / no2
    
    except ZeroDivisionError as Zobj:
        print("Divide By Zero is Not Allowed : ",Zobj)
        return
    
    except ValueError as vobj:
        print("Invalid Input:",vobj)
        return
    
    except Exception as Zobj:
        print("Exception occured as : ",Zobj)
        return 
    
    print("Division is : ",Ans)
    
if __name__ == "__main__":
    main()