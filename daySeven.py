print("Hello " + name + "!")
print("I am a affirmation genie! Please answer these questions to get your affirmation!")
continued = input("Do you wish to continue? ")
if continued == "yes" or continued == "Yes" :
  print("Okay! heres your first question. ")
  affirmation1 = input("What the current day of the week? ")
  if affirmation1 == "monday" or affirmation1 == "Monday":
      print("Monday's are the best! So heres your first question! ")
      mondayaffirmation1 = input("What is your favorite restaurant? ")
      print("I love " + mondayaffirmation1 + " too! You're the best. Great minds think alike")
  elif affirmation1 == "friday":
      print("Fridays are the best! So heres your first question! ")
      fridayaffirmation = input("What is your favorite friday activity? ")
      print("I love " + fridayaffirmation + " too! You're the best. Great minds think alike")   
  else:
      print("Thats a great day! Here are some more questions!")
      affirmation2 = input("What is your favorite animal? ")
      affirmation3 = input("What is your favorite color? ")
      print("Okay we have your two words to describe your affirmation. Kindness for" , affirmation2 , " and bold for" ,affirmation3)
else:
  print("Okay! Have a nice day!")