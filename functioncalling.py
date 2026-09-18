'''
Name: Benjamin Cohen
Python Week 03: Function Calling
I pledge my honor that I have abided by the Stevens Honor System.
Github Link: https://github.com/benjaminscohen/SSW540
'''

#student class
class Student:
  def __init__(self, name, courses):
    self.name = name
    self.courses = courses

#student creation
s1 = Student("Benjamin Cohen", 5)
s2 = Student("Anthony Reverri", 6)
s3 = Student("Irakli Dokhnadze", 2)
s4 = Student("Abdul Karim Mohammed", 1)
s5 = Student("Danica Chakroborty", 6)
s6 = Student("Charlotte Morcos", 2)
s7 = Student("Jason Bhalla", 5)
s8 = Student("Haoyang Liu", 8)
s9 = Student("John Doe", 1)

#functions
def fullTime(s):
  if (type(s.courses) is not int): raise TypeError("Number of student courses must be an integer")
  if (s.courses < 3): return False
  else: return True

def checkTime(s):
  if (fullTime(s) == True): print(s.name, "Full-time")
  elif (fullTime(s) == False): print(s.name, "Part-time")
  else: raise TypeError("Number of student courses must be an integer")

checkTime(s1)
checkTime(s2)
checkTime(s3)
checkTime(s4)
checkTime(s5)
checkTime(s6)
checkTime(s7)
checkTime(s8)
checkTime(s9)