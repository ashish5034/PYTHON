def lengthNo(nn):
    
    print(len(str(nn)))

def digitCount(num):
    count = 0
    while num != 0:
        num = num // 10
        count = count + 1
    return count

def countDigit(n):
    if n//10 == 0:
        return 1
    return 1 + countDigit(n // 10)       

def main():
    
    No = int(input())
    
    print(lengthNo(No))
    
    print(digitCount(No))
    
    print(countDigit(No))

    
if __name__ =="__main__":
    main()