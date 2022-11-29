import os
from data import data

def bold(text):
  print(f"\033[1m{text}\033[0m")

def newAccount():
  os.system("clear")
  bold("Create Account"); print()
  newUser = str(input("Username > ")); print()
  if newUser in data.keys():
    print("Username already exists. Please try again."); print()
    input("Press enter to continue "); __init__()
  elif len(newUser) > 15:
    print("Please create a username under 16 characters."); print()
    input("Press enter to continue "); __init__()
  elif len(newUser) < 3:
    print("Please create a username at least 3 characters long."); print()
    input("Press enter to continue "); __init__()
  else:
    newPassword = str(hash(input("Password > "))); print()
    if len(newPassword) < 3:
      print("Please create a password at least 3 characters long."); print()
      input("Press enter to continue "); __init__()
    else:
      try:
        message = str(input("Message > "))
        e = open(f"{newUser}.msg", "a+"); e.write(message); e.close()
        data[newUser] = newPassword
        f = open("data.py", "w"); f.write(str(f"data = {data}")); f.close()
      except:
        print("Error during account creation proccess. Please try again."); print()
        input("Press enter to continue "); __init__()
  
def login():
  os.system("clear")
  bold("Login"); print()
  inputUser = str(input("Username > ")); print()
  if inputUser not in data.keys():
    print("User does not exist. Please try again."); print()
    input("Press enter to continue "); __init__()
  else:
    inputPassword = str(hash(input("Password > "))); print()
    if data[inputUser] == inputPassword:
      print("Login successful!"); print()
      f = open(f"{inputUser}.msg", "r"); message = str(f.read()); f.close()
      print(f"Message: {message}"); print()
      input("Press enter to continue "); __init__()

def __init__():
  os.system("clear")
  bold("Secret Message Keeper"); print()
  print("1. Login"); print("2. Create Account"); print()
  mainInput = str(input("> "))
  if mainInput == str("1"):
    login()
  elif mainInput == str("2"):
    newAccount()
  else:
    __init__()

while True:
  __init__()
