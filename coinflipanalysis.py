# flexible coin flip analysis
# Jxcob-Vfx

# this script simulates flipping a coin by generating a pseudorandom integer; either 0 or 1

# import pseudorandom number generation data library
import random

heads = 0
tails = 0
# prompt user to input how many times they want the coin to be flipped (soft limit suggestion: around ten million)
values = int(input("How many values? > "))
print()
# prints "Loading..." to the user
# we're working with Python here, and it's not exactly speedy when it comes to large data tables
print("Loading...")
print()
# range(0,values) utilizes the user's prior input to the local variable "values"
for i in range(0, values):
  number = int(random.randint(0,1))
  # check if the number generated is 0 or 1 and change the value of "heads" or "tails" accordingly.
  if number == int(0):
    heads += 1
  elif number == int(1):
    tails += 1
  else:
    pass
print()
# print final totals to user
print(f"Heads: {heads}")
print(f"Tails: {tails}")
margin = 0
# calculate margin:
# (ie: 52, 48, margin would be 52 > 48, 52 - 48 = 4)
# note that the margin of 4 in this scenario would not reflect the drift from the median, which is 2:
# (52 + 48 = 100; 100 / (52) (48); 100 / 2, 50, 50 - 48 = 2)
if heads > tails:
  margin = heads - tails
elif tails > heads:
  margin = tails - heads
else:
  pass
# print margin to user with f string (f"{margin}")
print(f"Margin: {margin}")
# check if value inputted by user is even, then divide by 2 to find the median
if values % 2 == int(0):
  median = values / 2
  # calculate drift from median - drift is the same for heads and tails:
  # (ie: 50-48 = 2; 52 - 50 = 2) so we should subtract smaller number so that we don't need to get absolute value involved
  if heads > tails:
    drift = median - tails
  elif tails > heads:
    drift = median - heads
    # print drift from median to user with f string (f"{drift}")
    print(f"Drift from median: {drift}")
else:
  print("Unable to calculate drift because specified value not even")
