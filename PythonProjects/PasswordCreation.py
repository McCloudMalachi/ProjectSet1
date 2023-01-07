#Programmed by Malachi McCloud
#Date:11-28-2022
#CMIS 102 Week 6 Assignment
#Password Creation with Requirements
import re

#Establish and define a method to check for a space in the users input(password)
def one_word(password):
    if " " not in password:#If statement checking for a space
        return True #Return statement allowing for the password to be set and printed if it fits the parameter of having no spaces

#====================================================================================================================================================================================

#Establish and define a method to check for permited characters within in the password
def permitted_characters(password):
    numbers = 0 #Creating default value for the amount of numbers in the password
    letters = 0 #Creating a default value for the amount of letters in the password


    #For Loop
    for i in password: #Looping for I to check the input for letters and numbers
        #If statement check    
        if i.isdigit():#Checking for integers(numbers) in the password
            numbers += 1 #Adding a character to the count if it is existant to meet the parameter of one digit and one number
        #If statement check
        if i.isalpha():#Checking for letters in the password
            letters += 1 #Adding a character to the count if it is existant to meet the parameter of one digit and one number
        #Final if statement for the method
        if letters > 0 and numbers > 0: #Checking to see if the 1 letter and 1 number requirement for the password is met
            return True #Return statement allowing for the password to be set and printed if it fits the parameter of having atleast 1 letter and 1 number

#===================================================================================================================================================================================

#Establish and define our method for checking the length of the password
def check_length(password):
    #If Statement Check
    if len(password) >= 6 and len(password) <= 15:#Check for both parameters of being more than 6 characters and 15 or less characters.
        return True #Return statement allowing for the password to be set and printed if it fits the parameter of being more than 6 characters and 15 or less characters.

#===================================================================================================================================================================================

#Establish and define our main method
def main():
    password = input("Enter the password: ")#Ask for input for the user to establish their password
    if check_length(password) and permitted_characters(password) and one_word(password):#Run our password input through the checks
        print("Your password is valid.")#Statement if the password fits all 3 of the establish parameters
    else:
        print("Your password is invalid.")#Statement if the password fails any of the 3 parameters

#==================================================================================================================================================================================
#Run our main method
main()
