
name = input("What's your name?")
name=name.capitalize()
print("Hi " +name)

num_length=len(name)
num_length=str(num_length)
print("your name is " +num_length +" letters long")

firstL = name[0]
lastL = name[-1]
print("The first letter in your name is " +firstL + " and your last letter is "
      +lastL.capitalize())
otherL= name[1:-1]
print("and the other letters are " + otherL.upper())





