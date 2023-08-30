
import threading

def even():
    for i in range(2,21,2):
        print("Even:", i)
        
    
def odd():
    for i in range(1,20,2):
        print("Odd:", i)
        
    
def main():
    
    even = threading.Thread(target=even)
    
    odd = threading.Thread(target=odd)
    
    even.start()
    odd.start()
    even.join()
    odd.join()
    
if __name__ == "__main__":
    main()