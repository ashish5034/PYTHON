import threading

def addevenFactors(no):
    sum = 0
    even=[]
    for i in range (1,no+1):
        if no%i == 0 and i%2 == 0:
            sum = sum + i
            even.append(i)
    print(f"Even factors of {no}: ",even)
    print("Sum Of Even Factors: ",sum)
           
def addoddFactors(no):
    sum = 0
    odd = []
    for i in range (1,no+1):
        if no%i == 0 and i%2 !=0:
            sum = sum + i
            odd.append(i)
    print(f"Odd Factor of {no}: ",odd)
    print("Sum of Odd Factors: ",sum)  
         
def main():
    
    num = int(input("Enter Number: "))
    
    evenfactor = threading.Thread(target=addevenFactors, args=(num,))
    oddfactor = threading.Thread(target=addoddFactors, args=(num,))
    
    evenfactor.start()
    oddfactor.start()
    
    evenfactor.join()
    oddfactor.join()
    
if __name__ == "__main__":
    main()