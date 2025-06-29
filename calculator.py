


def calc():
    # add function 
    def add(num1,num2) -> float:
        return num1+num2

    # subtract function
    def sub(num1,num2) -> float:
        return num1-num2

    # multipy function
    def mul(num1,num2) -> float:
        return num1*num2

    # divide function
    def div(num1,num2) -> float:
        return num1/num2

    optn = int(input('select option\n 1. add\n 2. substract\n 3. multiplication \n 4. division\n\n'))
    if optn>=1 and optn<=4:
        number1=float(input("enter the number1: "))
        number2= float( input("enter the number2: "))    

    if optn==1:
        print(add(number1,number2))
    elif optn==2:
        print(sub(number1,number2))
    elif optn==3:
        print(mul(number1,number2))
    elif optn==4:
        print(div(number1,number2))
    else :
        print("Select from option only")
        
if __name__=='__main__':
    calc()


