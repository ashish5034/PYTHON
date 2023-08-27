
from functools import reduce


# def chkBw(No):
#     result = []
#     for val in No:
#         if val>=70 and val<=90:
#             result.append(val)
#     return result

check = lambda no:no>=70 and no<=90   

# def increase(No):
#     result=[]
#     val=0
#     for val in No:
#         val=val+10
#         result.append(val)
#     return result   

incr = lambda no: no+10
    
# def product(No):
#     mul=1
#     for val in No:
#         mul=mul*val
#     return mul
 
mult = lambda no1,no2:no1*no2
       
def main():
    data = []
    size = int(input("Enter size of list: "))
    for i in range (size):
        value = int(input())
        data.append(value)
    print("Input List = ",data)
    
    # ret = chkBw(data)
    # print("List after filter = ",ret)
     
    ans = list(filter(check,data))
    print("List after filter = ",ans) 
    
    # ret1 = increase(ans)
    # print("List after map= ",ret1)
    
    ans1 = list(map(incr,ans))
    print("List after map= ",ans1)
      
    # ret2 = product(ret1)
    # print("List after reduce= ",ret2)
      
    ans2 = reduce(mult,ans1)
    print("List after reduce= ",ans2)
    
if __name__ =="__main__":
    main()