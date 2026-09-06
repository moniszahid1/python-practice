#try:
#    user_input=input("Enter a number ")
#    number=float(user_input)
#    result=100/number
#    print(f"you number is {result}")
#except ZeroDivisionError:
#    print("Error:Could not divide by zero")
#except ValueError:
#    print("provide correct value")

#try:
#    with open("data.txt", "r") as m:
#        content=m.read()
#        print(content)
#except FileNotFoundError:
#    print("File Not founds")
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Operation attempted")