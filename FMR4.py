# unnamed func (lambada func/anonymous func)
# name = lambda Parameter -list:function_logic
def Add(No1,No2):
    return No1 + No2

AddX = lambda No1,No2 : No1 + No2

def checkEven(No):
    return(No % 2 == 0)

checkEvenX = lambda No : (No % 2 == 0)

def Increase(No):
    return No + 2

IncreaseX = lambda No :No + 2


def main():
    Ret = Add(10,11)
    print(Ret)
    
    Ret = checkEven(10)
    print(Ret)
    
    Ret = Increase(10)
    print(Ret)
    
    Ret = AddX(10,11)
    print(Ret)
    
    Ret = checkEvenX(10)
    print(Ret)
    
    Ret = IncreaseX(10)
    print(Ret)
    
if __name__ == "__main__":
    main()