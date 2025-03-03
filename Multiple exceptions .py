try:
    num1, num2=eval(input("Enter two numbers,, seperating by a comma :"))
    result=num1/num2
    print("Result is",result)
     
except ZeroDivisionError :
    print("Division by 0 is error !!")

except SyntaxError :
    print("Comma is missing. Enter number seperated by comma like this 1, 2")

except :
    print("Wrong input")

else :
    print("no exception")

finally :
    print("This code will excecute no matter what !")