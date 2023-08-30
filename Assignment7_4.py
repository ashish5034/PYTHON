import threading
import os
def count_small_chars(string):
    count = 0
    for char in string:
        if char.islower():
            count = count + 1
    
    print("PID of Task1 is : ",os.getpid())     
    print(f"Small Thread - ID: {threading.get_ident()}, Name: {threading.current_thread().name}")
    print(f"Number of small characters: {count}")

def count_capital_chars(string):
    count = 0 
    for char in string:
        if char.isupper():
            count = count + 1
    
    print("PID of Task1 is : ",os.getpid())        
    print(f"Capital Thread - ID: {threading.get_ident()}, Name: {threading.current_thread().name}")
    print(f"Number of capital characters: {count}")

def count_digits(string):
    count = 0
    for char in string:
        if char.isdigit():
            count = count + 1
    
    print("PID of Task1 is : ",os.getpid())
    print(f"Digits Thread - ID: {threading.get_ident()}, Name: {threading.current_thread().name}")
    print(f"Number of digits: {count}")

def main():
    input_string = input("Enter a string: ")

    small_thread = threading.Thread(target=count_small_chars, args=(input_string,))
    capital_thread = threading.Thread(target=count_capital_chars, args=(input_string,))
    digits_thread = threading.Thread(target=count_digits, args=(input_string,))

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("All threads have finished.")
if __name__ == "__main__":
    main()