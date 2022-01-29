#Python script to find greatest among three numbers

num1 = float(input("Enter your number : "))
num2 = float(input("Enter your number : "))
num3 = float(input("Enter your number : "))

if (num1>num2) and (num1>num3):
    print("the greater number is", num1)

elif (num2>num1) and (num2>num3):
    print("the greater number is", num2)

else:
    print("the greater number is", num3)    


