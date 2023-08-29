class BookStore:
    
    NoOfBooks = 0
    
    def __init__(self,Name,Author):
        # self.Name = input("Enter Book Name: ")
        # self.Author = input("Enter Book Author Name: ") 
        self.Name = Name
        self.Author = Author
        
        BookStore.NoOfBooks=BookStore.NoOfBooks + 1
            
    def Display(self):
        print("Name Of Book :   ",self.Name)
        print("Author Of Book:  ",self.Author)
        print("Number of Books: ",self.NoOfBooks)
    
def main():
    
    Obj1=BookStore("Linux System Programming","Robert Love")
    Obj1.Display()
    
    Obj2=BookStore("C Programming","Dennis Richie")
    Obj2.Display()
    
    # a=BookStore()
    # a.Display()
    
if __name__ == "__main__":
    main()