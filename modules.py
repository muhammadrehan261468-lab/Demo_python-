# import pyjokes

# print("Prints jokes")
# joke = pyjokes.get_joke()
# print(joke)

# print('''
#       A quiet breeze at close of day,
# Softly carries thoughts away.
# Dreams take root where shadows fall,
# Whispers of hope embrace us all.
#       ''')

# import pyttsx3

# engine = pyttsx3.init()
# engine.say("""Faraz KALA HA Faraz KALA HA Faraz KALA HA 
#               Faraz KALA HA Faraz KALA HA Faraz KALA HA 
#            """)
# engine.runAndWait()

# import os

# # specify the path (you can change this to any directory you want)
# path = "."

# try:
#     # list all files and folders in the directory
#     contents = os.listdir(path)
#     print(f"Contents of directory '{path}':")
#     for item in contents:
#         print(item)
# except FileNotFoundError:
#     print(f"The directory '{path}' does not exist.")
# except PermissionError:
#     print(f"Permission denied to access '{path}'.")
# import time

# def my_function():
#     for i in range(1000000):  
#         pass                   # 'pass' ka matlab hai kuch na karna (sirf loop ghoomega)

# start = time.time()     # yahan se time record kiya my_function()           # function run kar diya
# end = time.time()       # yahan time record kiya (function khatam hone ke baad)

# print("Running time:", end - start, "seconds")

########## Variables in python #########
# a = True
# b = False
# c =  a and b
# print(c)

# a = "31.4"

# b = float(a) # a but the type should be float 

# c = type(a)
# t = type(b)
# print(t,c)

# a = int(input("Enter number a "))
# b = int(input("Enter number b "))

# print("Number a:", a)
# print("Number b:", b)

# print("Sum of Numbers is:", a + b)

# a = 64
# b = 3
# print("Remainder when a is divided by b is :", a % b)

# a = float(input("Enter a number    "))
# t = type(a)
# print(t)

# a = int(input("Enter Number a  "))
# b = int(input("Enter Number b  "))

# print(" a is grater then b :", a > b)

# a = int(input("Enter Number a  "))
# b = int(input("Enter Number b  "))

# print("Average of the numbers is  :", (a + b)/2)

# a = int(input("Enter Number a  "))

# print("Square of the numbers is  :", a**2)

# name = "Rehan"

# shortName = name[0:3]
# Name = name[3]
# Name2 = name[4]

# print(shortName)
# print(Name)
# print(Name2)