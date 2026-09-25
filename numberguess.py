'''
Name: Benjamin Cohen
Python Week 04: Number Guessing Game
I pledge my honor that I have abided by the Stevens Honor System.
Github Link: https://github.com/benjaminscohen/SSW540
'''
import random
import sys
import time

#prompt user input
print("\n" "Host: Hello, I am the host of this game. Please input a secret number between 0 and 50.")
time.sleep(0.7)
secret = input("\n" + "User: ")
time.sleep(0.5)
print("\n" + "Pre-program validity testing..." + "\n")
time.sleep(1)
print("...")
time.sleep(1)
print("..." + "\n")
time.sleep(1)

#validate input
try:
  secret = int(secret)
  valid = secret >= 0 and secret < 51
  if (valid == False):
     print("Host: User! Your secret number must be between 0 and 50!" + "\n")
     time.sleep(1)
     sys.exit("Restart the program to try again" + "\n")
except ValueError:
   print("Host: User! Your secret number must be a valid integer!" + "\n")
   time.sleep(1)
   sys.exit("Restart the program to try again" + "\n")

time.sleep(1)
print("Host: Valid input! Beginning game now..." + "\n")
time.sleep(1)
print("...")
time.sleep(1)
print("..." + "\n")
time.sleep(1)
print("Computer: Hello! I am the computer. I'm going to begin by guessing a random number between 0 and 50.")
time.sleep(1)
print("Computer: If my guess is incorrect, please indicate whether your secret number is higher or lower than my guess!")

#random generation of initialGuess
initialGuess = random.randint(0, 50)
time.sleep(2)
print(f"Computer: I guess that your number is {initialGuess}!")
time.sleep(1)
print("Computer: Let me confer with the host to see if my guess was correct!")

#check higher or lower
def higherOrLower(string, guess, min, max):
  if (string == "higher"):
    if (secret < guess):
       print("\n" + "Host: Cheat!" + "\n")
       time.sleep(0.8)
       print("Computer: You Cheater!" + "\n")
       time.sleep(1)
       sys.exit("Cheaters don't get to play. Goodbye." + "\n")
    min = guess + 1
  elif (string == "lower"):
    if (secret > guess):
       print("\n" + "Host: Cheat!" + "\n")
       time.sleep(0.8)
       print("Computer: You Cheater!" + "\n")
       time.sleep(1)
       sys.exit("Cheaters don't get to play. Goodbye." + "\n")
    max = guess - 1
  else:
    print("\n" + "Host: Sorry User! The only accepted inputs are 'higher' or 'lower'! Try again" + "\n")
    return guess, min, max
  
  time.sleep(1)
  guess = random.randint(min, max)
  print("\n" f"Computer: I guess that your number is {guess}!")
  return guess, min, max

min = 0
max = 50

#main loop
while initialGuess != secret:
     time.sleep(2)
     print("\n" + f"Host: Computer! Your guess, {initialGuess}, was incorrect! Too bad :)" + "\n")
     time.sleep(2)
     print("Computer: :(")
     time.sleep(1)
     print("Computer: User! Was your secret number higher or lower than my guess?:" + "\n")
     time.sleep(1)
     higherLower = input("User: ")
     time.sleep(1)
     initialGuess, min, max = higherOrLower(higherLower, initialGuess, min, max)

time.sleep(2)
print(f"Host: Computer! Your guess, {initialGuess} was correct!" + "\n")
time.sleep(1)
print("Computer: Awesome! Good game User!" + "\n")
time.sleep(1)
print("Host: Good game User! Run this program again if you want to play another round!" + "\n")
time.sleep(1)
print("Computer: Goodbye for now!" + "\n")