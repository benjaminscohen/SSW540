'''
Name: Benjamin Cohen
Python Week 05: String Manipulation
I pledge my honor that I have abided by the Stevens Honor System.
Github Link: https://github.com/benjaminscohen/SSW540
'''
import sys
import time

message = input("Insert security message: ")

if (len(message) > 140):
  sys.exit("Your message must be 140 letters or less")

def cypher(string):
  #spaces position array
  count = 0
  space_pos = []
  for char in string:
    if char.isspace():
      space_pos.append(count)
    count = count + 1

  #convert string to capital letters
  array = string.split()
  for i in range(len(array)):
    array[i] = array[i].upper()
  array = ''.join(array)
  return array, space_pos

def decypher(string, array):
  new_string = ""
  string = string.lower()
  string_index = 0

  for i in range(len(string) + len(array)):
    if i in array:
      new_string = new_string + " "
    else:
      new_string = new_string + string[string_index]
      string_index = string_index + 1
  new_string = new_string.capitalize()

  return new_string

time.sleep(1)
print("Cyphering message..." + "\n")
time.sleep(1)

cyphered_message, space_array = cypher(message)
print(f"Your cyphered text is: {cyphered_message}")
time.sleep(1)
print(f"Exact string indexes where the spaces used to be: {space_array}" + "\n")
time.sleep(2)

print("Now Decyphering message..." + "\n")
time.sleep(1)
decyphered_message = decypher(cyphered_message, space_array)
print(f"Decyphered message: {decyphered_message}")
print("Goodbye" + "\n")