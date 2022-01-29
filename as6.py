#Python script to display the number of days in a given month


month = int(input("Enter your month : "))
year = int(input(" Enter your year : "))
monthlist = [1,3,5,7,9,11]

if month==2 and year % 4==0 :
    print("Number of days in a given month is 29")
elif month == 2:
    print("Number of days in a given months is 28 ")    
elif month in monthlist:
    print("Number of days in a given month is 31")
else:
    print("Nimber of days in a given year is 30")    

