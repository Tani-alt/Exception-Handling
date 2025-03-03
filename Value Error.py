#Exception handiling
try:
    n=int(input("Enter a number:"))
    print("the number is", n)
except ValueError as ex :
    print("Exception", ex)