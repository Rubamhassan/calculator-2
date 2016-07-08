"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


user_input = ""

while True:
    user_input = raw_input("What math questions would you like to ask? If you would like to quit press 'q'\n")  
    if user_input == 'q':
        break
    user_split = user_input.split(" ")
    user_split[1] = int(user_split[1])
    user_split[2] = int (user_split[2])
    
    if user_split[0] == "+":
        added = add(user_split[1], user_split[2])
        print added
        user_input
    # break

    elif user_split[0] == "-":
        substracted = subtract(user_split[1],user_split[2])
        print substracted

    elif user_split[0] == "*":
        multiplied = multiply(user_split[1],user_split[2])
        print multiplied 

    elif user_split[0] == "/":
        divided = divide(user_split[1],user_split[2])
        print divided

    elif user_split[0] == " **":
        squared = square(user_split[1])
        print squared

    elif user_split[0] == "**3":
        cubed = cube(user_split[1])
        print cubed

    # elif user_split[0] == "**" num2:
    #     power(user_split[1],user_split[2])

    elif user_split[0] == "%":
        moded = mod(user_split[1],user_split[2])    
        print moded

    else:
        print "error"    
