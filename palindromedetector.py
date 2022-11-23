# Jxcob-Vfx 2022
# palindrome detector

# import data library
import os as screen;

# defene string reverse function
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

# define simple bold print function
def bold(b):
  print(f"\033[1m{b}\033[0m")

# define main function
def __init__():
  screen.system("clear") # os
  bold("Palindrome Detector"); print()
  s = input("Word > "); print()
  # check if user input \s\ is equal to the reversed string
  # note the use of \str(s.lower())\ instead of \str(s)\ to ensure accuracy
  if str(s.lower()) == str(reverse(s.lower())):
    # print response to end user
    print(f"{s} is a palindrome"); print()
  else:
    print(f"{s} is not a palindrome"); print()
  input("Press enter to continue ")

# loop main function
while True:
  __init__()
