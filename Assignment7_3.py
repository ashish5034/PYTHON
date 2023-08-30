import threading
def even(no):
    even=[]
    sum = 0
    for i in no:
        if i%2 == 0:
            even.append(i)
            sum = sum + i
    print("Even Number In List: ",even)
    print("Sum Of Even Number In List: ",sum)
    
def odd(no):
    odd=[]
    sum = 0
    for i in no:
        if i%2 != 0:
            odd.append(i)
            sum = sum + i
    print("Odd Number In List: ",odd)
    print("Sum Of Odd Number In List: ",sum)

def main():
    size = int(input("Enter size of list: "))
    data = []
    for i in range (size):
        val = int(input())
        data.append(val)
    print("Input List: ",data)
    
    evenlist = threading.Thread(target=even, args=(data, ))
    oddlist = threading.Thread(target=odd, args=(data, ))
    
    evenlist.start()
    oddlist.start()
    evenlist.join()
    oddlist.join()
    
if __name__ == "__main__":
    main()