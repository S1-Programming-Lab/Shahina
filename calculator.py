from pakagecalc.calc import *
while True:
    print("select option")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.division")
    print("5.exit")
    
    num1=int(input("enter the first number:"))
    num2=int(input("enter thesecond number:"))

    choice = input("enter your choice")
    if choice=="1":
        print(num1,"+",num2,"=",addition(num1,num2))
    elif choice=="2":
        print(num1,"-",num2,"=",subtraction(num1,num2))
    elif choice=="3":
        print(num1,"*",num2,"=",multiplication(num1,num2))
    elif choice=="4":
        print(num1,"/",num2,"=",division(num1,num2))
    
    else:
        print("invalid choice")
        break
    


