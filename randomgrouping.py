'''
Name: Benjamin Cohen
Python Week 02: Random Grouping
I pledge my honor that I have abided by the Stevens Honor System.
Github Link: https://github.com/benjaminscohen/SSW540
'''

import random

#unsorted list of students
students = ["Benjamin Cohen", "Anthony Reverri", "Irakli Dokhnadze", 
            "Abdul Karim Mohammed","Danica Chakroborty", "Charlotte Morcos", "Jason Bhalla", "Haoyang Liu", "John Doe"]

#list init
last_names = []

#split and append last name
for student in students:
  try:
    split = student.split()
    last_names.append(split[-1])
  except IndexError:
    print("Error: no student name")
    exit()

#alphabetically sorted list
sorted = last_names.copy()
sorted.sort()

original = last_names.copy()

#loop logic
while True:
  #reset in cases where group conflicts
  group1 = []
  group2 = []
  group3 = []
  last_names = original.copy()

  #random shuffling of unsorted list
  try:
    random.shuffle(last_names)
  except TypeError:
    print("Error: list cannot be shuffled")
    exit()

  for members in last_names.copy():
    if (len(group1) == 3):
      break
    if (len(group1) == 0):
      group1.append(members)
      last_names.remove(members)
    else:
      adjacent = False
      for member in group1:
        try:
          index = sorted.index(members)
          index2 = sorted.index(member)
        except ValueError:
          print("Error: student not in list")
          exit()
        if (index == index2 + 1 or index == index2 - 1):
          adjacent = True
          break
      if (adjacent == False):
        group1.append(members)
        last_names.remove(members)

  for members in last_names.copy():
    if (len(group2) == 3):
      break
    if (len(group2) == 0):
      group2.append(members)
      last_names.remove(members)
    else:
      adjacent = False
      for member in group2:
        try:
          index = sorted.index(members)
          index2 = sorted.index(member)
        except ValueError:
          print("Error: student not in list")
          exit()
        if (index == index2 + 1 or index == index2 - 1):
          adjacent = True
          break
      if (adjacent == False):
        group2.append(members)
        last_names.remove(members)

  for members in last_names.copy():
    if (len(group3) == 3):
      break
    if (len(group3) == 0):
      group3.append(members)
      last_names.remove(members)
    else:
      adjacent = False
      for member in group3:
        try:
          index = sorted.index(members)
          index2 = sorted.index(member)
        except ValueError:
          print("Error: student not in list")
          exit()
        if (index == index2 + 1 or index == index2 - 1):
          adjacent = True
          break
      if (adjacent == False):
        group3.append(members)
        last_names.remove(members)
  
  if (len(group1) == 3 and len(group2) == 3 and len(group3) == 3):
    break

print('\n')
print('Group 1:')
print(group1)
print('\n')

print('Group 2:')
print(group2)
print('\n')

print('Group 3:')
print(group3)
print('\n')