# Prompt the user to input a year
year = int(input("Enter a year: "))

# Using if statements, output whether the inputted year is or is not a leap year
if (year % 100 == 0):
  if (year % 400 == 0):
    print (str(year) + " is a leap year.")
  else:
    print (str(year) + " is not a leap year.")

elif (year % 4 == 0):
  print (str(year) + " is a leap year.")

else:
  print (str(year) + " is not a leap year.")