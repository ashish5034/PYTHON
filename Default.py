# default argument
def Display(Name, Age, Marks=90):
    print("Name is :",Name)
    print("Age is :", Age)
    print("Marks are: ",Marks)


def main():
    print("Demonstration of Default arguments")
    Display("Amit",25)   
    Display("Sagar",24,78)
    
if __name__ == "__main__":
    main()