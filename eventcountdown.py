# Jxcob-Vfx
# event countdown

# import data libraries
import datetime, os

# define simple bold printing function
def bold(text):
  print(f"\033[1m{text}\033[0m")

# define function to calculate days until preset events
# this function takes 4 arguements as integers that allow it to calculate the number of days until an event
def presetDelta(name, year, month, day):
  date = datetime.date.today()
  # create date with arguements
  event = datetime.date(year, month, day)
  # calculate the difference between today's date \date\ and the preset date from the arguements \event\
  difference = event - date
  difference = difference.days
  os.system("clear")
  # identify if the event is in the past, present, or future
  # in the first 2 if statements, nested statements ensure that if only one day is remaining to an event, a custom message will be printed
  if event > date:
    if difference != 1:
      print(f"{difference} days until {name}"); print()
    else:
      print(f"{name} is tomorrow"); print()
  elif event < date:
    if difference != 1:
      print(f"{name} was {difference} days ago"); print()
    else:
      print(f"{name} was yesterday"); print()
  elif event == date:
    print(f"{name} is today")
  else:
    os.system("clear")
    bold("Error evaluating date. Please try again."); print()
    input("Press enter to continue ")
    preset()
  input("Press enter to continue ")
  __init__()
 
# define function to calculate time until an end-user-specified date
def main():
  os.system("clear")
  bold("Custom Event"); print()
  try:
    # attempt to take user input with try in case of string instead of integer or invalid date
    name = str(input("Name of event > ")); print()
    year = int(input("Year > ")); print()
    month = int(input("Month > ")); print()
    day = int(input("Day > ")); print()
    event = datetime.date(year, month, day)
    date = datetime.date.today()
    difference = event - date
    difference = difference.days
    # identical difference calculation script
    if event > date:
      if difference != 1:
        print(f"{difference} days until {name}"); print()
      else:
        print(f"{name} is tomorrow"); print()
    elif event < date:
      if difference != 1:
        print(f"{name} was {difference} days ago"); print()
      else:
        print(f"{name} was yesterday"); print()
    elif event == date:
      print(f"{name} is today")
    else:
      os.system("clear")
      bold("Error evaluating date. Please try again."); print()
      input("Press enter to continue ")
      main()
    input("Press enter to continue ")
  except:
    print("Invalid date specified. Please try again."); print()
    input("Press enter to continue ")
    main()

# subroutine for menu of preset event dates
def preset():
  os.system("clear")
  bold("Preset Event"); print()
  print("1. Christmas"); print("2. New Year's Eve"); print("3. Valentine's Day"); print("4. Halloween"); print("5. Next Year"); print("6. Menu"); print()
  presetInput = str(input("> "))
  # the year values will need to be manually updated to ensure accuracy
  # note the passing of 4 arguements: \name\, \year\, \month\, and \day\.
  if presetInput == str("1") or presetInput == str("1."):
    presetDelta("Christmas", 2022, 12, 25)
  elif presetInput == str("2") or presetInput == str("2."):
    presetDelta("New Year's Eve", 2022, 12, 31)
  elif presetInput == str("3") or presetInput == str("3."):
    presetDelta("Valentine's Day", 2023, 2, 14)
  elif presetInput == str("4") or presetInput == str("4."):
    presetDelta("Halloween", 2023, 10, 31)
  elif presetInput == str("5") or presetInput == str("5."):
    presetDelta("Next Year", 2023, 1, 1)
  elif presetInput == str("6") or presetInput == str("6."):
    __init__()
  else:
    os.system("clear")
    bold("Error"); print()
    print("Invalid menu selection. Please try again."); print()
    input("Press enter to continue ")
    preset()

# primary menu function for loop
def __init__():
  os.system("clear")
  bold("Event Countdown"); print()
  print("1. Preset Event"); print("2. Custom Event"); print()
  inp = str(input("> "))
  if inp == str("1") or inp == str("1."):
    preset()
  elif inp == str("2") or inp == str("2."):
    main()
  else:
    os.system("clear")
    bold("Error"); print()
    print("Invalid menu selection. Please try again."); print()
    input("Press enter to continue ")
    __init__()

# run primary function
while True:
  __init__()
