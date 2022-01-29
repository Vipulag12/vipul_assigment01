#Python script to calculate Simple Interest.


p = float(input("Enter your number : "))
r = float(input("Enter your number : "))
t = float(input("Enter your number : "))

si = p*r*t % 100 #formula
print("The simple inerest of given number is" , si)