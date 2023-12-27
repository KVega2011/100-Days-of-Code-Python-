print("hello! welcome to the how many seconds are in a year calculator!")
leapYear = input("Is it a leap year?")
seconds = 60
minutes = 60 * seconds
hours = 24 * minutes
days = 365 * hours
if leapYear == "yes":
  days = 366 * hours
  print("There are",days,"in a year")
else:
  print("There are",days,"in a year")