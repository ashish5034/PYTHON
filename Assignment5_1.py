class Demo:
    def __init__(self,no1,no2):
        # print("inside constructor")
        self.value=no1
        self.value=no2
        
    def fun(self):
        print(self.value,self.value)
    
    def gun(self):
        print(self.value,self.value)
        
def main():
    # print("Inside Main")
    obj1=Demo(11,21)
    obj2=Demo(51,10)
    
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()
    
if __name__=="__main__":
    main()