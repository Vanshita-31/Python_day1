import random 
import time

# Print random number using inbuilt random function 
RandomNum = random.randint(10,100)
print(RandomNum)


# List
fruits = ["Banana", "Apple", "Mango"]
veggies = ["Tomatoes", "Potatoes", "Cucumber"]

#daily_dozen = [fruits, veggies]
# print(daily_dozen)

# print(daily_dozen[1][1])


'''
for i in veggies:
    print (i)
    time.sleep(5)
    
'''



# Arithmetic Operators
# '+' , '-' , '*' , '/' , '//'
# '/' -> Dividies the number as is
# '//' -> Rounds off the number


#print(2==2 & 2==3) # Comparison Operator 'and , &' ;  
   
'''
name = input("Enter you Name : ")
age = int(input("Enter your Age : "))
activity = ["Drive", "Vote"]
if age >= 18:
    print(f"{name} Wohooo! You can now : {activity}") # f"" -> Template Literal 
elif age == 17:
    print("You are almost 18! Wait till you turn 18")
else:
    print("Sorry, You cannot Vote")

'''


# Even Number: 
for i in range(51):
    if i%2 == 0:
        print(i)















