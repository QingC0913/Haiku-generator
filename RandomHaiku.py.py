#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
threeLine1 = ["The moon rose", "The sun rose"]
fiveLine = ["The flower falls down", "The ocean waves crash"]
threeLine2 = ["The stars shone", "The birds sing"]
#Generates a random integer.
aRandomIndex = randint(0, len(threeLine1)-1)
aRandomIndex2 = randint(0, len(fiveLine)-1)
aRandomIndex3 = randint(0, len(threeLine2))

answer = input("If you would like a randomly-assembled haiku, Type ok.")
if answer == "ok":
    print ("Your haiku is")
    print (threeLine1[aRandomIndex])
    print (fiveLine[aRandomIndex2])
    print (threeLine2 [aRandomIndex3])
