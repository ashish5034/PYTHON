
def Add(A,B): #0x00000267B79B04A0>
    return A+B

# Function accept  parameters and  another funtion
def Marvellous(FPTR1):
    print(type(FPTR1))
    print(FPTR1)
    Ans = FPTR1(11,7)  #Ans = 0x00000267B79B04A0(11,7)  ->Hashcode of add function
    print("Addition is :",Ans)

def main():
    Marvellous(Add) #Marvellous(0x00000267B79B04A0)
   
if __name__ == "__main__":
    main()