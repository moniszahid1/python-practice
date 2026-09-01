numbers=int(input("Enter a number of your choice "))
if numbers%2==0:
    print(f"provided number {numbers} is even")
else:
    print(f"provided number {numbers} is odd")
if numbers>0:
    print(f"provided number {numbers} is positive")
elif numbers<0:
    print(f"provided number {numbers} is negative")
else:
    print(f"provided number {numbers} is zero")


