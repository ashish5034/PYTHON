# def primeNo(data1):
#     ansList = []
#     for num in data1:
#         if num == 0 or num == 1 :
#             continue
#         for i in range(2, num) :
#             if num % i == 0 :
#                 break
#         else:
#             ansList.append(num)
#     return ansList  

from functools import reduce


primeNo = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

# def multiply(data1):
#     result=[]
#     for val in data1:
#         val=val*2
#         result.append(val)
#     return result

multiply =lambda num: num*2

# def maximumNo(data1):
#     for val in data1:
#         a=max(data1)
#     return a 

maxiNo = lambda num1,num2: max(num1,num2)

def main():
    data=[]
    size=int(input("Enter size of list: "))
    print("Enter the element in list: ")
    for i in range(size):
        value=int(input())
        data.append(value)
    print("Input List=",data)
    
    primeNum = list(filter(primeNo,data))
    print("List after filter : ",primeNum)
    
    # ans = primeNo(data)
    # print("List after filter= ",ans)
    
    mult =list(map(multiply,primeNum))
    print("List after map= ",mult)
    
    # mult =multiply(ans)
    # print("List after ma=:",mult) 
    
    max = reduce(maxiNo,mult)
    print("Output of reduce= ",max)
    
    # max = maximumNo(mult)
    # print("Output of reduce=",max)
    
if __name__ == "__main__":
    main()
    