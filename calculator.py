


while True:
 
 inputContinue = input("Press 'Y' to continue your calculations" ).lower()

 if inputContinue != 'y':
    break

 input1 = int(input("Enter first Number : "))
 input2 = int(input("Enter second Number : "))
 operator = input("Enter an Operator : '+', '-', '*' , '/' :  ")

 if operator == '+':
    print(input1 + input2)
 elif operator == '-':
    print(input1 - input2)
 elif operator == '*':
    print(input1 * input2)
 elif operator == '/':
    print(input1 / input2)
 else :
    print("Please check your inputs")


 inputClose = input("Press 'X' to terminate the calculation").lower()
 if inputClose == "X":
    break


    



    

