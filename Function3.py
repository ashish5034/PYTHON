
# Function accept more parameter and return Nothing
def Marvellous(Name,Age,City):
    print("Inside Marvellous Function")
    print("Welcome: ",Name)
    print("Age is: ",Age)
    print("City: ",City)

def main():
    Marvellous('Amit',28,"pune")
    Marvellous(City="Mumbai",Age=30,Name="sagar")
if __name__ == "__main__":
    main()