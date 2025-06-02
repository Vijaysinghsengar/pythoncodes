operation=input("enter the execution y/n:")
while operation==y:
                num1=int(input("enter the first number:"))
                choose=input("enter the opetation : +  , - , * , / : ")
                num2=int(input("enter the second number:"))
                if choose =="+":
                        print(num1+num2)
                elif choose=="-":
                    print(num1-num2)
                elif choose=="*":
                    print(num1*num2)
                elif choose=="/":
                        print(num1/num2)
                else:
                        print("error!! you entered wrong operation")
else:
        operation==n
        

