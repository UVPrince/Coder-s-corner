invited=['amit','aman','abishek','amar']

name=input("enter your name: ")

if name.lower() in invited:
  print(name,", Welcome to the party")
  print("You were invited")
  
else:
  print("you are not invited")
