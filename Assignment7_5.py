import threading
def display1():
    for number in range (1,51,1):
        print(number,end=" ")
    print(" ")
def display2():
    for number in range(50, 0, -1):
        print(number, end=" ")

def main():
    
    thread1 = threading.Thread(target=display1)
    thread2 = threading.Thread(target=display2)
    
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
    
if __name__ == "__main__":
    main()