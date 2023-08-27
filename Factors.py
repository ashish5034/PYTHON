print("Enter Number : ")
No = int(input())

for n in range (1, No+1):
    if(No%n==0):
        print(n)
        n=n+1