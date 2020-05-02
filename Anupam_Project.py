# The project creates a password of length provided by the user as input

import random    #importing the random module


n=int(input("please enter the length of the password you require :-"))   #Taking the desired length of password as input

# creating pool of UpperCase,LowerCase,DigitS and Special characters


Upper_Case=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

Lower_Case= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Special_Characters=['@', '#', '$','&','%']

Pool_Of_Characters=Upper_Case+Lower_Case+Digits+Special_Characters

password=""

# loop for the formation of password

for x in range(1,n+1):
    random_character=random.choice(Pool_Of_Characters)
    password=password+random_character

print("Your Password is {}".format(password))






