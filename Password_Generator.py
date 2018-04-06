#-------------------------------------------#
# Author - Yash Gaurav                      #
# Date - 4/4/2018                           #
# Written in Python3                        #
# Email me @ razorcool000@gmail.com         #
# Feel free to make changes to this file    #
# Any help is appreciated                   #
#-------------------------------------------#

'''
Main function name - Password_Generator()
Param - None
Argument - None
'''

# Importing important libraries for the programme

import random, os

'''
random - To make random passwords from the alphabet and numbers provided
os - To clear the shell screen after every use
'''

# Main function starts here

def Password_Generator():
    os.system('clear')
    character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    password = ''
    print("Hello User! Press enter to generate a password for yourself or q to quit")
    decison = input()

    if decison == 'q':
       exit()
    else:
        x = int(input("Enter the length of your password : "))
        while x > 0:
            password = password + random.choice(character)
            x -= 1
    print("Your password is : " + password)
    input()
    Password_Generator()
    
# Call the function for the program to start

Password_Generator()