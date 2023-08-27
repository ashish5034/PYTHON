class Circle:
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))
        
    def CalculateArea(self):
        self.Area = self.PI * self.Radius ** 2
        
    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        
    def Display(self):
        print("Radius: ",self.Radius)
        print("Area: ",self.Area)
        print("Circumference: ",self.Circumference)

# Creating objects and using methods
def main():
    circle1 = Circle()
    circle1.Accept()
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    print("Details of Circle 1:")
    circle1.Display()
    print()

    circle2 = Circle()
    circle2.Accept()
    circle2.CalculateArea()
    circle2.CalculateCircumference()
    print("Details of Circle 2:")
    circle2.Display()

if __name__ == "__main__":
    main()