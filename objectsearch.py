'''
Name: Benjamin Cohen
Python Week 06: Object Search
I pledge my honor that I have abided by the Stevens Honor System.
Github Link: https://github.com/benjaminscohen/SSW540
'''
import random
import time
import sys

fruits = ["apple", "orange", "banana", "blueberry", "strawberry", "grape", "cherry", "peach", "mango", "lemon"]

num = input("How many objects (fruits) would you like to populate?: ")

if type(int(num)) is not int or int(num) < 0:
  print("Error: input must be a valid integer. Please Try again")
  sys.exit(1)

num = int(num)

print("\n" + "Populating array of random fruit objects...")
time.sleep(1)

random_fruits = random.choices(fruits, k=num)

print(f"Random fruits array: {random_fruits}")
time.sleep(1)
print("\n" + "Discovering unique objects (exist only once)..." + "\n")
time.sleep(2)

unique_objects = []
seen = []

for fruit in random_fruits:
  if fruit in seen:
    continue
  elif fruit in unique_objects:
    seen.insert(0, fruit)
    unique_objects.remove(str(fruit))
  else:
    unique_objects.insert(0, fruit)

print(f"Unique objects found: {unique_objects}" + "\n")


